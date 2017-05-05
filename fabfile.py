
from fabric.api import task, run, require, put, local, env, cd, prefix
from fabric.contrib.files import upload_template
from contextlib import contextmanager
import time

## DEFINE CONTEXT to config in SERVER
# NOTE: all private information should contains in other file (this file upload to git)
from khangvnblog.local_settings import FABRIC

env.hosts = FABRIC.get("HOSTS",[""])
env.user = FABRIC.get("SSH_USER","root")
env.password = FABRIC.get("SSH_PASS","")
env.key_filename = 'C:\Users\Quynh beautiful\Dropbox\KathyShop\OTHER documents\quantvnChicagoVPS_OpenSSH'
env.venv_home = "/home/%s/.virtualenvs" % env.user
env.venv_path = env.venv_home + "/%s" %env.user
if not hasattr(env, "proj_app"):
    env.proj_app = "khangvnblog"
env.activate = 'source %s/bin/activate' %env.venv_path
env.proj_path = '/home/%s/deploy/production' %env.user
env.locale = FABRIC.get("LOCALE", "en_US.UTF-8")
env.secret_key = FABRIC.get("SECRET_KEY","7bA2kvOj:w0S48I/>&+E]-f<>[#nUW")
env.nevercache_key = FABRIC.get("NEVERCACHE_KEY", ";2f(CdkO[^s~m8X_474.B;GG^A+b'_")

CHECKOUT_HOST = FABRIC.get("CHECKOUT_HOST","")
DEPLOY_WRAPPER_FOLDER = "/home/%s/deploy" %env.user
PRODUCTION_MAPPER = DEPLOY_WRAPPER_FOLDER + "/production" #should map with env.proj_path


@contextmanager
def _virtualenv():
    """
    Runs commands within the project's virtualenv.
    """
    with cd(env.venv_path):
        with prefix(env.activate):
            yield

@contextmanager
def _project(proj_path=env.proj_path):
    """
    Runs commands within the project's directory.
    """
    with _virtualenv():
        with cd(proj_path):
            yield

class __Deploy:

    deploy_dir = env.proj_path

    def deploy(self):
        self.test()
        # self.collect_static()
        # self.checkout_code()

        # self.install_system_packages()
        self.install_python_packages_requirement()
        # self.migrate_db()
        # self.collect_static()
        # self.map_new_deployment()

        # self.run_task_django()

    def test(self):
        run('uname -a')
        local("echo a")

    def checkout_code(self):

        self.deploy_dir = "{}/quantvn{}".format(DEPLOY_WRAPPER_FOLDER,time.strftime("%Y%m%d%H%M"))
        with cd(DEPLOY_WRAPPER_FOLDER):
            run("git clone {} {}".format(CHECKOUT_HOST, self.deploy_dir))


    def install_system_packages(self):
        packages = []
        if packages:
            run("apt-get install "+" ".join(packages))

    def install_python_packages_requirement(self):
        with _virtualenv():
            run("pip install -r {}/requirements.txt".format(self.deploy_dir))

    def migrate_db(self):

        run("python manage.py migrate")

    def collect_static(self):
        if not self.deploy_dir:
            self.deploy_dir = env.proj_path

        #run("cd %s"%self.deploy_dir)
        # run("python manage.py collectstatic")

    def run_task_django(self):
        with _project():
            run("python manage.py collectstatic -v 0 --noinput")
            #run("python manage.py migrate --noinput")

    def map_new_deployment(self):
        if self.deploy_dir != env.proj_path:
            run("rm %s" % PRODUCTION_MAPPER)
            run("ln -s {} {}".format(self.deploy_dir, PRODUCTION_MAPPER))
            run("restart quantvnapp")

    def create_or_local_settings(self):
        upload_template("deploy/local_settings.py.template",
                        "{}/{}/local_settings.py".format(self.deploy_dir, env.proj_app),
                        env, use_sudo=True, backup=False)

def deploy():
    __Deploy().deploy()

