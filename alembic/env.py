from logging.config import fileConfig

from sqlalchemy import pool
from alembic import context

# Import پروژه
from core.database import Base, engine
from user_role.models import UserRole  # همه‌ی مدل‌هایی که ساختی اینجا ایمپورت کن

# این همون alembic config هست
config = context.config

# لاگینگ
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# متادیتا برای autogenerate
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
