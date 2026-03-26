[app]

title = calculator
package.name = calcus
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy==2.3.0,kivymd,pillow

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a,armeabi-v7a
android.accept_sdk_license = True
android.skip_update = True

p4a.branch = develop

[buildozer]

log_level = 2
warn_on_root = 1
