[app]
title = Knight Saver
package.name = knightsaver
package.domain = com.ali.knightsaver
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0
orientation = landscape

[buildozer]
log_level = 1

[buildozer:android]
android.api = 33
android.minapi = 21
android.ndk = 28c
android.accept_sdk_license_agreement = True
android.ant = auto
