import os
from app import create_app
import click
from flask.cli import FlaskGroup


@click.command(cls=FlaskGroup, create_app=create_app)
def cli():
    """Main entry point."""
    if os.environ.get('FLASK_COVERAGE'):
        import coverage
        cov = coverage.coverage(branch=True, include='app/*')
        cov.start()

    env_name = os.getenv("FLASK_ENV", "development")
    app = create_app(env_name)

    if os.environ.get('FLASK_COVERAGE'):
        cov.stop()
        cov.save()
        print('Coverage Summary:')
        cov.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'coverage')
        cov.html_report(directory=covdir)
        print('HTML version: file://{}/index.html'.format(covdir))
        cov.erase()
    else:
        if __name__ == "__main__":
            app.run(debug=True, host="0.0.0.0", port=5000)
