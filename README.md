# my helper

Just a small repo to be included as a git submodule.

The package name can be the same as the repo name,
but here, they are distinguished in this case. The package name is `my_helper`.

A repo that becomes a git submodule or git subtree looks exactly the same as a repo on its own.

For simplicity, this repo has no docs folder.

Properties of different inclusion settings.

| main module distribution | build                                                       | build                                           | git                                                | git                                                                        | git                                                                           |
| ------------------------ | ----------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| sub module linked as     | build                                                       | git subtree or submodule                        | build                                              | git subtree                                                                | git submodule                                                                 |
| packages are created for | main and sub                                                | only main                                       | only sub                                           | no package                                                                 | no package                                                                    |
| distributed packages     | main and sub are separate                                   | only main, contains sub                         | only sub                                           | no package                                                                 | no package                                                                    |
| access needed            | pypi                                                        | pypi                                            | pypi + git                                         | git                                                                        | git                                                                           |
| debugable                | no                                                          | no                                              | only main                                          | main and sub                                                               | main and sub                                                                  |
| installed with           | 1xpip                                                       | 1xpip                                           | git + 1xpip                                        | git + 2xpip                                                                | git + 2xpip                                                                   |
| commits are sent         | n.a.                                                        | n.a.                                            | main                                               | main                                                                       | main or sub                                                                   |
| notes                    | easy to install, main and sup pkg are separately updateable | easy to install, sub pkg cannot be updated sep. | easy to develop main, pkg needs to be created sep. | the developer of main has full view over sub, pkg needs to be created sep. | the developer of main has full control over sub, pkg needs to be created sep. |
