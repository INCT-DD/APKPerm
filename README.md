## Android M Permissions Analysis
Tool to statically analyze permission references within decompiled Android M apps.

### Context
With the release of Android 6.0 (Android M / API Level 23), users can now grant system and 3rd party permissions at runtime instead of during installation.

This increases an application's susceptibility to over and underprivileging. If a normal (as opposed to [dangerous][1]) permission is defined in the app manifest, the system grants that permission automatically -- even if the app is not using the permission directly. However, users can grant all permissions, including dangerous, within a permission group by requiring a single permission. This may result in overprivileging. For convenience, design and further documentation is [in the wiki][5].

#### Rules to Keep in Mind
1. If an app requests a **normal** permission it will be granted immediately. [View the list of normal permissions here](http://developer.android.com/guide/topics/security/normal-permissions.html).
2. If an app requests a **dangerous** permission listed in its manifest, and the app already has another dangerous permission in the same permission group, the system immediately grants the permission without any interaction with the user.
3. Permissions defined in the manifest and never referenced in source are considered **overprivileged**.
4. Permissions not defined in the manifest, and refereneced in the source, are considered **underprivileged**. 

### Setup
MPermission requires Python 3.0 - 3.4. 

MPermission uses pre-written decompilation scripts from the kocsenc/android-scraper project. The project is referenced via a [submodule](3). After cloning the project, it can be installed via:

```bash
% git submodule init
% git submodule update
```

After cloning and updating the submodule, run  

```bash
% python3 android-scraper/tools/apk-decompiler/setupDependencies.py
```
This will install dex2jar and apktools for the android-scraper. For further Android decompilation instructions, refer to [the README](4) within the submodule.

Now install any package dependencies:  
```bash
% pip install -r requirements.txt
```

You should now be ready to decompile and analyze some Android M apps.

### Usage  

The tool can be run incrementally with the following flags:

```bash
% python3 mperm.py -d [--decompile] apk_path              # decompiles APK and moves it to sample_apk/
% python3 mperm.py -a [--analyze]   decompiled_apk_path   # analyze and prints source report / analysis report
```

[1]: http://developer.android.com/guide/topics/security/permissions.html#normal-dangerous
[2]: https://www.wikiwand.com/en/Android_application_package
[3]: https://git-scm.com/book/en/v2/Git-Tools-Submodules
[4]: https://github.com/kocsenc/android-scraper/tree/master/tools/apk-decompiler/
[5]: https://github.com/dan7800/MPermission/wiki
