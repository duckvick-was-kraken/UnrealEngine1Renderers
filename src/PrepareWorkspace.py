# -*- mode: python ; coding: utf-8 -*-
try:
    from pathlib import Path
    import sys
    import ssl
    import urllib.request
    import certifi  #non-standard
    import os
    import errno
    import shutil
    from zipfile import ZipFile
    import subprocess
    import patchpy #non-standard
except Exception as e:
    print('ERROR: importing', e)
    raise


def DownloadFile(url, dest, callback=None):
    # still do this on dryrun because it writes to temp?
    sslcontext = ssl.create_default_context(cafile=certifi.where())
    old_func = ssl._create_default_https_context
    ssl._create_default_https_context = lambda : sslcontext # HACK

    print('\n\ndownloading', url, 'to', dest)
    urllib.request.urlretrieve(url, dest, callback) # "legacy interface"
    print('done downloading ', url, 'to', dest)

    ssl._create_default_https_context = old_func

def CheckHeaderExistence(headerfolder,gamename):
    testfile = headerfolder / gamename / 'Core' / 'Inc' / 'Core.h'
    return testfile.exists()

def CheckDXSDKExistence(sdkdir):
    testfile = sdkdir / 'Include' / 'd3d9.h'
    return testfile.exists()

def ExtractSDK(infile,tmpdir,outdir):

    if infile.exists()==False:
        print("SDK file does not exist")
        return

    #Fuck it, we need to use 7z externally
    print("Extracting SDK...")
    subprocess.run(["7z","x","-aoa",infile, "-o"+str(tmpdir)])

    print("Moving SDK...")
    shutil.copytree(tmpdir/"DXSDK",outdir,dirs_exist_ok=True)
    print("SDK Moved!")
    infile.unlink()

def ExtractZip(filename,outdir):
    if (filename.exists()==False):
        return False

    zip = ZipFile(filename, 'r')
    zip.extractall(outdir)
    zip.close()
    (filename).unlink()
    return True

def ExtractHeaders(tmpdir,gamesdir,patchdir,headers):
    print("Extracting headers")
    headersdir = tmpdir/'GameHeaders'

    if headers["DeusEx"]==False or \
       headers["Rune"]==False or \
       headers["Rune_100"]==False or \
       headers["Unreal_226_Gold"]==False or \
       headers["UnrealTournament"]==False:
        if ExtractZip(tmpdir/'headers.zip', headersdir):
            if headers["DeusEx"]==False:
                shutil.copytree(headersdir/'Games'/'DeusEx',gamesdir/'DeusEx',dirs_exist_ok=True)
            if headers["Rune"]==False:
                shutil.copytree(headersdir/'Games'/'Rune',gamesdir/'Rune',dirs_exist_ok=True)
            if headers["Rune_100"]==False:
                shutil.copytree(headersdir/'Games'/'Rune_100',gamesdir/'Rune_100',dirs_exist_ok=True)
            if headers["Unreal_226_Gold"]==False:
                shutil.copytree(headersdir/'Games'/'Unreal_226_Gold',gamesdir/'Unreal_226_Gold',dirs_exist_ok=True)
            if headers["UnrealTournament"]==False:
                shutil.copytree(headersdir/'Games'/'UnrealTournament',gamesdir/'UnrealTournament',dirs_exist_ok=True)

    if (headers["Unreal_224"]==False):
        if ExtractZip(tmpdir/'unreal224.zip', headersdir/'Unreal_224'):
            print("Patching Unreal_224")
            ApplyPatch(headersdir/"Unreal_224",patchdir/"Unreal_224.patch")
            shutil.copytree(headersdir/'Unreal_224',gamesdir/'Unreal_224',dirs_exist_ok=True)

    if (headers["Nerf"]==False):
        if ExtractZip(tmpdir/'nerf.zip', headersdir/'Nerf'):
            shutil.copytree(headersdir/'Nerf',gamesdir/'Nerf',dirs_exist_ok=True)

    if (headers["Klingon"]==False):
        if ExtractZip(tmpdir/'klingon.zip', headersdir/'Klingon'):
            print("Patching Klingon")
            ApplyPatch(headersdir/"Klingon",patchdir/"Klingon.patch")
            shutil.copytree(headersdir/'Klingon',gamesdir/'Klingon',dirs_exist_ok=True)

    if (headers["HarryPotter"]==False):
        if ExtractZip(tmpdir/'harrypotter.zip', headersdir/'HarryPotter'):
            print("Patching HarryPotter")
            ApplyPatch(headersdir/"HarryPotter",patchdir/"HarryPotter.patch")
            shutil.copytree(headersdir/'HarryPotter',gamesdir/'HarryPotter',dirs_exist_ok=True)

    if (headers["XComEnforcer"]==False):
        if ExtractZip(tmpdir/'xcom.zip', headersdir/'XComEnforcer'):
            print("Patching XComEnforcer")
            ApplyPatch(headersdir/"XComEnforcer",patchdir/"XComEnforcer.patch")
            shutil.copytree(headersdir/'XComEnforcer',gamesdir/'XComEnforcer',dirs_exist_ok=True)

    if (headersdir.exists()):
        shutil.rmtree(headersdir)

def ApplyPatch(targetdir,patchfile):
    if targetdir.exists()==False:
        print("Couldn't find patch target: "+str(targetdir))
        return
    if patchfile.exists()==False:
        print("Couldn't find patch file: "+str(patchfile))
        return

    print("Applying patch "+str(patchfile)+" to dir "+str(targetdir))

    diff = patchpy.DiffFile.from_path(patchfile)
    diff.fix_counts()
    diff.validate()
    diff.apply(root=targetdir)
        




#------------------------------------------------------------------------------------------#


downloads = {}
base = Path(sys.argv[0]).parents[0] #Directory that this script lives in
tmpdir = base/'tmp'
headerdir = base/'Games'
patchdir = base/'HeaderPatches'
dxsdkdir = base/'dxsdk-jun2010'
patchdir = base/'HeaderPatches'

targets=["UnrealTournament","XComEnforcer","DeusEx","Rune","Rune_100","Unreal_226_Gold","Unreal_224","Nerf","HarryPotter","Klingon"]
headers={}
for target in targets:
    headers[target]=CheckHeaderExistence(headerdir,target)
headers["dxsdk"]=CheckDXSDKExistence(dxsdkdir)

#Check to see if extracted headers already exist
if headers["DeusEx"]==False or \
   headers["Rune"]==False or \
   headers["Rune_100"]==False or \
   headers["Unreal_226_Gold"]==False or \
   headers["UnrealTournament"]==False:
    
    downloads["https://www.kentie.net/article/d3d10drv/files/src/games.zip"]="headers.zip" #DeusEx, Rune, Rune_100, Unreal_226_Gold, UnrealTournament

if (headers["Unreal_224"]==False):
    downloads["https://coding.hanfling.de/launch/mirror/unrealpubsrc224v.zip"]="unreal224.zip" #Unreal_224

if (headers["Nerf"]==False):
    downloads["https://coding.hanfling.de/launch/nonofficial/NerfPubSrc12_20150507.zip"]="nerf.zip" #Nerf

if (headers["Klingon"]==False):
    downloads["https://coding.hanfling.de/launch/nonofficial/KlingonsPubSrc11_20150326.zip"]="klingon.zip" #Klingon

if (headers["HarryPotter"]==False):
    downloads["https://coding.hanfling.de/launch/nonofficial/HarryPotterPubSrc11_20170323.zip"]="harrypotter.zip" #HarryPotter

if (headers["XComEnforcer"]==False):
    downloads["https://coding.hanfling.de/launch/nonofficial/XComEnforcerPubSrc10_20161002.zip"]="xcom.zip" #XComEnforcer

#Check if extracted DirectX SDK already exists
if (headers["dxsdk"]==False):
    downloads["https://download.microsoft.com/download/a/e/7/ae743f1f-632b-4809-87a9-aa1bb3458e31/DXSDK_Jun10.exe"]="dxsdk.exe" #DirectX SDK, June 2010


if not tmpdir.exists():
    os.mkdir(tmpdir)

for (url, dest) in downloads.items():
    p = tmpdir/dest
    if not p.exists():
        DownloadFile(url, p)


if headers["dxsdk"]==False:
    ExtractSDK(tmpdir/'dxsdk.exe',tmpdir,dxsdkdir)

ExtractHeaders(tmpdir,headerdir,patchdir,headers)

sys.exit()
#Remove tmp files
print("Cleaning tmp files")
try:
    shutil.rmtree(tmpdir)
    print("    Cleaned up")
except OSError as e:
    if (e.errno==errno.ENOENT):
        print("    Already Clean")
    else:
        print("    Failed to clean directory: %s" % (e.strerror))
