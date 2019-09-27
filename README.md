# rq-dashboard-on-heroku

[![rq-dashboard](https://img.shields.io/badge/rq--dashboard-v0.5.3-blue?style=flat-square)][pipfile]
[![python](https://img.shields.io/badge/python--dashboard-v0.5.3-blue?style=flat-square)][pipfile]
[](https://img.shields.io/github/l/metabolize/rq-dashboard-on-heroku?style=flat-square)
[![build](https://img.shields.io/circleci/project/github/metabolize/rq-dashboard-on-heroku?style=flat-square)][build]
[![code style](https://img.shields.io/badge/code%20style-black-black.svg?style=flat-square)][black]

[![code style](https://img.shields.io/badge/code_style-prettier-ff69b4?style=flat-square)][prettier]
[![lerna](https://img.shields.io/badge/maintained%20with-lerna-cc00ff?style=flat-square)][lerna]

[pipfile]: https://github.com/metabolize/rq-dashboard-on-heroku/blob/master/Pipfile
[build]: https://circleci.com/gh/metabolize/rq-dashboard-on-heroku/tree/master
[black]: https://black.readthedocs.io/en/stable/

A version of [RQ Dashboard][] that can be deployed to Heroku.

[rq dashboard]: https://github.com/eoranged/rq-dashboard


## Deployment

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


## Configuration

Three configuration settings are required:

- `RQ_DASHBOARD_REDIS_URL=rediss://redis:6379`
- `RQ_DASHBOARD_USERNAME=user`
- `RQ_DASHBOARD_PASSWORD=pass`


## License

This project is licensed under the 2-clause BSD license.
