[buildozer]
log_level = 1

[app]
title = Knight Saver
package.name = knightsaver
package.domain = com.ali.knightsaver
source.dir = .
version = 1.0
requirements = python3,kivy==2.3.0
orientation = landscape

[buildozer:android]
android.api = 33
android.minapi = 21
android.ndk = 28c
android.accept_sdk_license_agreement = True
