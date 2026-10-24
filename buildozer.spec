[app]
title = Knight Saver
package.name = knightsaver
package.domain = com.ali.knightsaver
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,pygame
orientation = landscape

[buildozer]
# Log chota rakho taake truncate na ho
log_level = 1

[buildozer:android]
android.api = 33
android.minapi = 21
android.ndk = 28c
android.sdk = 33
android.build_tools_version = 37.0.0
android.accept_sdk_license_agreement = True
# Sirf ek architecture build karo, time aur RAM bachega
android.arch = arm64-v8a
