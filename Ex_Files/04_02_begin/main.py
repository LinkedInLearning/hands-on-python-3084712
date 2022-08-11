from distutils.debug import DEBUG

from pkg_resources import DEVELOP_DIST

DEVELOPMENT = "development"
PRODUCTION = "production"
STAGING = "staging"


current_env = DEVELOPMENT

if current_env == DEVELOPMENT:
    print("Development environment")
elif current_env == PRODUCTION:
    print("Production environment")
elif current_env == STAGING:
    print("Staging environment")
else:
    print("Unknown environment")
