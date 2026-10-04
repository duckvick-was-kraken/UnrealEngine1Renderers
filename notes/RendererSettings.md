# Renderer Settings

This page should explain all of the settings available in the renderers. 

✅ = Setting is available on this renderer

❌ = Setting is NOT available on this renderer

| Setting Name | Direct3D 9 | Direct3D 10 | OpenGL | Description |
| ------------ | :--------: | :---------: | :----: | ----------- |
| 16BitTextures | ✅ | ❌ | ✅ | ? |
| 565Textures | ✅ | ❌ | ❌ | ? |
| AlphaPalette | ❌ | ❌ | ✅ | ? |
| AlphaToCoverage | ❌ | ✅ | ❌ | ? |
| Anisotropy | ✅ | ✅ | ✅ | ? |
| Antialiasing | ✅ | ✅ | ✅ | ? |
| AutoFOV | ❌ | ✅ | ❌ | ? |
| BGRATextures | ❌ | ❌ | ✅ | ? |
| Brightness | ✅ | ❌ | ✅ | ? |
| BufferTileQuads | ❌ | ❌ | ✅ | ? |
| BumpMapping | ❌ | ✅ | ❌ | ? |
| CacheStaticMaps | ✅ | ❌ | ✅ | ? |
| ClassicLighting | ❌ | ✅ | ❌ | ? |
| ClipboardScreenshots | ❌ | ✅ | ❌ | ? |
| DebugDrawDetailTextures | ✅ | ❌ | ✅ | ? |
| DecalDepthBias | ❌ | ✅ | ❌ | ? |
| DeferredRecording | ✅ | ✅ | ❌ | ? |
| DetailClipping | ✅ | ❌ | ✅ | ? |
| DetailMax | ✅ | ❌ | ✅ | ? |
| DetailTextures | ✅ | ❌ | ✅ | ? |
| DynamicTexIdRecycleLevel | ✅ | ❌ | ✅ | ? |
| FragmentProgram | ✅ | ❌ | ✅ | ? |
| FrameRateLimit | ✅ | ✅ | ✅ | ? |
| GammaOffset | ✅ | ✅ | ✅ | ? |
| GammaOffsetBlue | ✅ | ❌ | ✅ | ? |
| GammaOffsetGreen | ✅ | ❌ | ✅ | ? |
| GammaOffsetRed | ✅ | ❌ | ✅ | ? |
| GenerateMipMaps | ✅ | ❌ | ❌ | ? |
| HardwareGamma | ✅ | ❌ | ✅ | ? |
| Instancing | ❌ | ✅ | ❌ | ? |
| LightmapAtlas | ✅ | ✅ | ❌ | ? |
| LODBias | ✅ | ✅ | ✅ | ? |
| MaxLogTextureSize | ✅ | ❌ | ✅ | ? |
| MaxTMUnits | ✅ | ❌ | ✅ | ? |
| MinLogTextureSize | ✅ | ❌ | ✅ | ? |
| MultiDrawArrays | ❌ | ❌ | ✅ | ? |
| MultiTexture | ✅ | ❌ | ✅ | ? |
| NoAATiles | ✅ | ❌ | ✅ | ? |
| NoFiltering | ✅ | ❌ | ✅ | ? |
| OneXBlending | ✅ | ✅ | ✅ | ? |
| Palette | ❌ | ❌ | ✅ | ? |
| ParallaxOcclusionMapping | ❌ | ✅ | ❌ | ? |
| PostProcessAA | ❌ | ✅ | ❌ | ? |
| Precache | ✅ | ✅ | ✅ | ? |
| PureDevice | ✅ | ❌ | ❌ | ? |
| ReduceBanding | ✅ | ✅ | ✅ | ? |
| RefreshRate | ✅ | ❌ | ✅ | ? |
| RenderThreads | ✅ | ✅ | ❌ | ? |
| S3TC | ✅ | ❌ | ✅ | Enables support for S3TC (Texture Compression).  When disabled, high resolution textures may look incorrect.  Requires restarting the game after changing the setting. |
| ShareLists | ❌ | ❌ | ✅ | ? |
| SingleCpuAffinity | ❌ | ✅ | ❌ | ? |
| SinglePassDetail | ✅ | ❌ | ✅ | ? |
| SinglePassFog | ✅ | ❌ | ✅ | ? |
| SmoothMaskedTextures | ✅ | ❌ | ✅ | ? |
| SoftwareVertexProcessing | ✅ | ❌ | ❌ | ? |
| SurfaceBatching | ✅ | ❌ | ❌ | ? |
| TexDXT1ToDXT3 | ✅ | ❌ | ✅ | ? |
| TexIdPool | ✅ | ❌ | ✅ | ? |
| TexPool | ✅ | ❌ | ✅ | ? |
| TextureCacheBudgetMegs | ✅ | ✅ | ✅ | ? |
| TextureFiltering | ❌ | ✅ | ❌ | Set to 0 gives point filtering, 1 gives linear filtering, 2 gives anisotropic filtering |
| Trilinear | ✅ | ❌ | ✅ | ? |
| TripleBuffering | ✅ | ❌ | ❌ | ? |
| UnlimitedViewDistance | ❌ | ✅ | ❌ | ? |
| UseSSE | ✅ | ❌ | ✅ | ? |
| UseSSE2 | ✅ | ❌ | ✅ | ? |
| VBO | ❌ | ❌ | ✅ | ? |
| VSync | ✅ | ✅ | ✅ | In D3D9/OpenGL, -1 respects the driver setting, 1 enables VSync, 2 allows half-rate (twice the frame rate).  In D3D10, this can just be enabled or disabled. |
| ZRangeHack | ✅ | ❌ | ✅ | ? |
| ZTrick | ❌ | ❌ | ✅ | ? |
