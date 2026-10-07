# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path
import os
import sys
import subprocess
import shutil
import errno


#region Build D3D9
def BuildD3D9(filepath):
    buildscript = filepath / 'build.bat'
    success = []
    fail = []
    print(buildscript)

    targets=["UnrealTournament","XComEnforcer","DeusEx","Rune","Rune_100","Unreal_226_Gold","Unreal_224","Nerf","HarryPotter","Klingon"]
    for target in targets:
        print(target)
        p = subprocess.Popen(str(buildscript)+" "+target, shell=True)
        stdout, stderr = p.communicate()

        if (p.returncode==0):
            print("Build Succeeded")
            success.append(target)
        else:
            print("Build Failed!")
            fail.append(target)

        print(" ")

    print("D3D9:")
    print("--------------")
    if (len(success)>0):
        print("Succeeded: "+str(success))

    if (len(fail)>0):
        print("Failed: "+str(fail))

    return {"success":success, "fail":fail}
#endregion

#region Build OpenGL
def BuildOpenGL(filepath):
    buildscript = filepath / 'build.bat'
    success = []
    fail = []
    print(buildscript)

    targets=["release UnrealTournament","release XComEnforcer","release DeusEx","release Rune","release Rune_100","release Unreal_226_Gold","release Unreal_224","release Nerf","release HarryPotter","release Klingon"]
    for target in targets:
        print(target)
        p = subprocess.Popen(str(buildscript)+" "+target, shell=True)
        stdout, stderr = p.communicate()

        if (p.returncode==0):
            print("Build Succeeded")
            success.append(target)
        else:
            print("Build Failed!")
            fail.append(target)

        print(" ")

    print("OpenGL:")
    print("--------------")
    if (len(success)>0):
        print("Succeeded: "+str(success))

    if (len(fail)>0):
        print("Failed: "+str(fail))

    return {"success":success, "fail":fail}
#endregion

#region Build D3D10
def BuildD3D10(filepath):
    buildscript = filepath / 'build.ps1'
    success = []
    fail = []
    print(buildscript)

    targets=["Deus Ex Release", "Harry Potter Release", "Nerf Arena Blast Release", "Klingon Release", "Rune 1.00 Release", "Rune Release", "Unreal 224 Release", "Unreal Gold Release", "Unreal Tournament Release", "X-COM Enforcer Release"]
    for target in targets:
        print(target)
        cmd = 'powershell.exe -file '+str(buildscript)+' -Configuration "'+target+'"'

        p = subprocess.Popen(cmd, shell=True)
        stdout, stderr = p.communicate()

        if (p.returncode==0):
            print("Build Succeeded")
            success.append(target)
        else:
            print("Build Failed!")
            fail.append(target)

        print(" ")

    print("D3D10:")
    print("--------------")
    if (len(success)>0):
        print("Succeeded: "+str(success))

    if (len(fail)>0):
        print("Failed: "+str(fail))

    return {"success":success, "fail":fail}
#endregion

#----------------------------------------------------------------------#

#region Clean Directories
def CleanBuildDirectories(dirs):
    print("")
    print("Cleaning Build Directories")
    print("----------------------------------------------")
    for dir in dirs:
        print("Cleaning Directory: "+str(dir))
        try:
            shutil.rmtree(dir)
            print("    Cleaned")
        except OSError as e:
            if (e.errno==errno.ENOENT):
                print("    Already Clean")
            else:
                print("    Failed to clean directory: %s" % (e.strerror))
#endregion

#region Collect Results
def CollectBuildResults(basedir):
    print("")
    print("Collecting build results...")

    targets=["UnrealTournament","XComEnforcer","DeusEx","Rune","Rune_100","Unreal_226_Gold","Unreal_224","Nerf","HarryPotter","Klingon"]

    d3d9dir = basedir / "D3D9" / "System"
    opengldir = basedir / "OpenGL" / "System"
    d3d10dir = basedir / "D3D10" / "packages"
    renderdirs = [d3d9dir, opengldir, d3d10dir]

    #Make sure the output directory exists (or create it if not)
    distdir = basedir / ".." / "dist"

    create = True
    if (os.path.exists(distdir)):
        if (os.path.isdir(distdir)):
            create=False
            print(str(distdir)+" exists already")
        else:
            print(str(distdir)+" exists, but it's a file???")
            distdir.unlink()

    if create:
        os.mkdir(distdir)
        print("Created "+str(distdir))

    for target in targets:
        targetdir = distdir / target

        #Collect all the renderers into a directory
        for render in renderdirs:
            renderdir = render / target
            print(str(renderdir) + " ---> " + str(targetdir))
            shutil.copytree(renderdir,targetdir, dirs_exist_ok=True)

        #Zip the contents of the target up
        shutil.make_archive(distdir / target,'zip',targetdir)
        print("Packaged "+target+ " into ZIP")

        try:
            shutil.rmtree(targetdir)
            print("Cleaned "+target+" directory")
        except OSError as e:
            if (e.errno==errno.ENOENT):
                print(target+" did not exist?")
            else:
                print("Failed to clean up directory: %s" % (e.strerror))
        print("")

#endregion

#----------------------------------------------------------------------#

#region Run Build

#The location of this python file
#Should be in the src directory
base = Path(sys.argv[0]).parents[0]



#Clean output directories
builddirs = []
#Delete these for a full clean rebuild
builddirs.append(base / "D3D9" / "Build")
builddirs.append(base / "OpenGL" / "Build")
builddirs.append(base / "D3D10" / "_work")
#Delete these to guarantee the contents are a fresh build
builddirs.append(base / "D3D9" / "System")
builddirs.append(base / "OpenGL" / "System")
builddirs.append(base / "D3D10" / "packages")
#Clean the packaging directory
builddirs.append(base / ".." / "dist")
#Actually clean them
CleanBuildDirectories(builddirs)


#Actually do the builds
d3d9=None
opengl=None
d3d10=None

d3d9 = BuildD3D9(base / 'D3D9')
opengl = BuildOpenGL(base / 'OpenGL')
d3d10 = BuildD3D10(base / 'D3D10')

print("")
print("")
print("")
print("Final Build Results:")
print("------------------------")
if (d3d9!=None):
    print("")
    print("D3D9:")
    print("Success: "+str(d3d9.get("success","")))
    print("Fail: "+str(d3d9.get("fail","")))

if (opengl!=None):
    print("")
    print("OpenGL:")
    print("Success: "+str(opengl.get("success","")))
    print("Fail: "+str(opengl.get("fail","")))

if (d3d10!=None):
    print("")
    print("D3D10:")
    print("Success: "+str(d3d10.get("success","")))
    print("Fail: "+str(d3d10.get("fail","")))

#Copy files to packaging folder
CollectBuildResults(base)


#endregion