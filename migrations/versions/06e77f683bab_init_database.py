"""init database

Revision ID: 06e77f683bab
Revises: 
Create Date: 2018-07-31 16:06:55.377819

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06e77f683bab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('phone', sa.String(length=11), nullable=True),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('role', sa.SmallInteger(), nullable=True),
    sa.Column('resume', sa.String(length=64), nullable=True),
    sa.Column('upload_resume', sa.String(length=64), nullable=True),
    sa.Column('is_disable', sa.Boolean(), nullable=True),
    sa.Column('real_name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_resume'), 'user', ['resume'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('company',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('slug', sa.String(length=24), nullable=False),
    sa.Column('logo', sa.String(length=64), nullable=False),
    sa.Column('site', sa.String(length=64), nullable=False),
    sa.Column('contact', sa.String(length=24), nullable=False),
    sa.Column('email', sa.String(length=24), nullable=False),
    sa.Column('location', sa.String(length=24), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('about', sa.String(length=1024), nullable=True),
    sa.Column('tags', sa.String(length=128), nullable=True),
    sa.Column('stack', sa.String(length=128), nullable=True),
    sa.Column('team', sa.String(length=256), nullable=True),
    sa.Column('welfare', sa.String(length=256), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_company_name'), 'company', ['name'], unique=True)
    op.create_index(op.f('ix_company_slug'), 'company', ['slug'], unique=True)
    op.create_table('job',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=24), nullable=True),
    sa.Column('low', sa.Integer(), nullable=False),
    sa.Column('high', sa.Integer(), nullable=False),
    sa.Column('tags', sa.String(length=128), nullable=True),
    sa.Column('experience', sa.String(length=32), nullable=True),
    sa.Column('degree', sa.String(length=32), nullable=True),
    sa.Column('types', sa.Boolean(), nullable=True),
    sa.Column('up', sa.Boolean(), nullable=True),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('status',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.SmallInteger(), nullable=True),
    sa.Column('response', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['job.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_job',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['job.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_job')
    op.drop_table('status')
    op.drop_table('job')
    op.drop_index(op.f('ix_company_slug'), table_name='company')
    op.drop_index(op.f('ix_company_name'), table_name='company')
    op.drop_table('company')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_resume'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
