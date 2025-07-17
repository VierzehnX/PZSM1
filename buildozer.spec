
[app]

title = PZSM
package.name = pzsm
package.domain = org.playzona
source.dir = .
source.include_exts = py,json,xlsx

version = 0.1
requirements = python3==3.7.6,hostpython3==3.7.6,kivy,requests
orientation = portrait
fullscreen = 1
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
osx.python_version = 3.7.6
osx.kivy_version = 1.9.1

[buildozer]

log_level = 2
warn_on_root = 1
