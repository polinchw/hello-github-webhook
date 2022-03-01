## [3.1.2](https://github.com/polinchw/hello-github-webhook/compare/v3.1.1...v3.1.2) (2022-03-01)


### Bug Fixes

* New build pipeline for VCS Test issue Fixes [#13](https://github.com/polinchw/hello-github-webhook/issues/13) ([f6fd90c](https://github.com/polinchw/hello-github-webhook/commit/f6fd90c2d6961ddbc137d2b5c82e1013edee9382))
* New build pipeline for VCS Test issue Fixes [#13](https://github.com/polinchw/hello-github-webhook/issues/13) ([2222b4d](https://github.com/polinchw/hello-github-webhook/commit/2222b4d6b44f821f4398378d2a2c2f6be53b776b))
* New build pipeline for VCS Test issue Fixes [#13](https://github.com/polinchw/hello-github-webhook/issues/13) ([1b94a9b](https://github.com/polinchw/hello-github-webhook/commit/1b94a9bcbde31f2d070a4848952d3815926200b4))
* Remove mr on push [#13](https://github.com/polinchw/hello-github-webhook/issues/13) ([ab13cf9](https://github.com/polinchw/hello-github-webhook/commit/ab13cf922dab840b5381b2f813477097c779b99b))
* Updating gitignore. ([46a6797](https://github.com/polinchw/hello-github-webhook/commit/46a67972e7d6c2b162695ac40d08285c677ba05d))
* VCS Test issue ([f6c8578](https://github.com/polinchw/hello-github-webhook/commit/f6c8578afd3c87a3a68c0228cbb034d2a5a79af3)), closes [#13](https://github.com/polinchw/hello-github-webhook/issues/13)



## [3.1.1](https://github.com/polinchw/hello-github-webhook/compare/v3.1.0...v3.1.1) (2022-01-08)


### Bug Fixes

* **docker-image-dev:** Comment out pull_request. ([7ca14f0](https://github.com/polinchw/hello-github-webhook/commit/7ca14f0cd857345a375731b9f652014974a36687))
* **docker-image-dev:** Use dev** for pull_requests. ([e32e564](https://github.com/polinchw/hello-github-webhook/commit/e32e564b20ca4081c4af52da8eecf6a21f40b39f))
* **docker-image-dev:** Use the dynamic branch name. ([8990040](https://github.com/polinchw/hello-github-webhook/commit/8990040fb68cb5dd1b075fea97329cd4015ffa14))
* **docker-image-dev.yml:** Build all dev pattern branches. ([3db4162](https://github.com/polinchw/hello-github-webhook/commit/3db41629e3b16ca12a2736bf9d133c2aa70c6969))
* **readme:** Changed the technology name from webhook to actions. ([fbdc5f1](https://github.com/polinchw/hello-github-webhook/commit/fbdc5f11dd27256963514c30654daae1e49080d4))
* **test:** Remove the test.yml ([8c77133](https://github.com/polinchw/hello-github-webhook/commit/8c77133dea96c1eaf1d50e9fbe67a97abdc61d28))



# [3.1.0](https://github.com/polinchw/hello-github-webhook/compare/v3.0.0...v3.1.0) (2021-12-23)


### Features

* **readme:** Adding ArgoCD to the readme. ([1ab010c](https://github.com/polinchw/hello-github-webhook/commit/1ab010c47c36a0374c3bf05e06fb69126f0400a3))



# [3.0.0](https://github.com/polinchw/hello-github-webhook/compare/v1.0.0...v3.0.0) (2021-12-23)


### Bug Fixes

* **docker-image-dev:** Adding test to main. ([140e092](https://github.com/polinchw/hello-github-webhook/commit/140e09260ee3ee0699d709fe8b4eceab2dc8c53e))
* **docker-image-dev:** Adding unit tests. ([0738526](https://github.com/polinchw/hello-github-webhook/commit/07385260dfbae78efe31e4db4cb91d5bd850ee2d))
* **docker-image-dev:** Use python to run the test. ([b254026](https://github.com/polinchw/hello-github-webhook/commit/b2540265e991a7ae2a6b2829b1f4ad5167ad72e9))
* **docker-image-dev:** Use python to run the test. ([1a7b005](https://github.com/polinchw/hello-github-webhook/commit/1a7b0059b23276e75fadc3ce9cbbff4983c8d0c5))
* **docker-image-main:** Setting tag prefix to v. ([2601f0a](https://github.com/polinchw/hello-github-webhook/commit/2601f0a347af2c0ba67652cd894345ead3d36e48))
* **docker-image-main:** Setting tag prefix to v. ([b507dbd](https://github.com/polinchw/hello-github-webhook/commit/b507dbdd54c3ac92c1969d352d83e2d543856b07))
* **test:** Adding tests for MRs. ([5fe58a5](https://github.com/polinchw/hello-github-webhook/commit/5fe58a50a8bc1c3532f7bc352e84643d0edcc222))
* **test:** Adding tests for MRs. ([cfdd58a](https://github.com/polinchw/hello-github-webhook/commit/cfdd58af3fd3b654e61717329bb4d039ebf2324a))
* **test:** Adding tests for MRs. ([7885927](https://github.com/polinchw/hello-github-webhook/commit/788592783261d68a5793a1af35cd09df858c16f8))
* **test:** Test all branches. ([9e68063](https://github.com/polinchw/hello-github-webhook/commit/9e680633c23021cad4e08a24b09d3bbd0783ebde))


### Features

* No tag prefix. ([16b3616](https://github.com/polinchw/hello-github-webhook/commit/16b36169eb2fdddd507394029c8de95979841292))
* No tag prefix. ([17f5310](https://github.com/polinchw/hello-github-webhook/commit/17f5310b17fc5a771900988b47efa5f23d3312a9))


### BREAKING CHANGES

* **docker-image-dev:** Adding tests.  Going back to v prefix.
* `extends` key in config file is now used for extending other config files
* `extends` key in config file is now used for extending other config files



# [1.0.0](https://github.com/polinchw/hello-github-webhook/compare/v0.1.33...v1.0.0) (2021-12-23)


### Features

* allow provided config object to extend other configs ([80be764](https://github.com/polinchw/hello-github-webhook/commit/80be76459574aea6bf437ca0e4cac7c9d6996d88))


### BREAKING CHANGES

* `extends` key in config file is now used for extending other config files



