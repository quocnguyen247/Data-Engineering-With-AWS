from datetime import datetime, timedelta
import pendulum
import os
from airflow.decorators import dag
from airflow.operators.dummy import DummyOperator
from airflow.operators.postgres_operator import PostgresOperator
from operators import (StageToRedshiftOperator, LoadFactOperator,
                       LoadDimensionOperator, DataQualityOperator)
from helpers import SqlQueries


start_date = datetime(2024, 6, 1)
end_date = datetime(2024, 6, 30)


s3_bucket = "udacity-dend-demo"
events_s3_key = "log-data"
songs_s3_key = "song-data/A/A/"
log_json_file = 'log_json_path.json'

default_args = {
    'owner': 'udacity',
    "depends_on_past": False,
    'start_date': pendulum.now(),
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
    "catchup": False,
    'email_on_retry': False
}

@dag(
    default_args=default_args,
    description='Load and transform data in Redshift with Airflow',
    schedule_interval='0 * * * *'
)
def final_project():

    start_operator = DummyOperator(task_id='Begin_execution')

    create_tables = PostgresOperator(
        task_id='create_tables',
        postgres_conn_id="redshift",
        sql='create_tables.sql',
    )

    stage_events_to_redshift = StageToRedshiftOperator(
        task_id='Stage_events',
        table="staging_events",
        redshift_conn_id="redshift",
        aws_credentials_id="aws_credentials",
        s3_bucket=s3_bucket,
        s3_key=events_s3_key,
        log_json_file=log_json_file
    )

    stage_songs_to_redshift = StageToRedshiftOperator(
        task_id='Stage_songs',
        table="staging_songs",
        redshift_conn_id="redshift",
        aws_credentials_id="aws_credentials",
        s3_bucket=s3_bucket,
        s3_key=songs_s3_key
    )

    load_songplays_table = LoadFactOperator(
        task_id='Load_songplays_fact_table',
        redshift_conn_id="redshift",
        sql_query=SqlQueries.songplay_table_insert
    )

    load_user_dimension_table = LoadDimensionOperator(
        task_id='Load_user_dim_table',
        redshift_conn_id="redshift",
        sql_query=SqlQueries.user_table_insert
    )

    load_song_dimension_table = LoadDimensionOperator(
        task_id='Load_song_dim_table',
        redshift_conn_id="redshift",
        sql_query=SqlQueries.song_table_insert
    )

    load_artist_dimension_table = LoadDimensionOperator(
        task_id='Load_artist_dim_table',
        redshift_conn_id="redshift",
        sql_query=SqlQueries.artist_table_insert
    )

    load_time_dimension_table = LoadDimensionOperator(
        task_id='Load_time_dim_table',
        redshift_conn_id="redshift",
        sql_query=SqlQueries.time_table_insert
    )

    run_quality_checks = DataQualityOperator(
        task_id='Run_data_quality_checks',
        redshift_conn_id = "redshift",
        tables = ["songplays", "users", "songs", "artists", "time"]
    )

    end_operator = DummyOperator(task_id='Stop_execution')

    start_operator >> create_tables >> [stage_events_to_redshift, stage_songs_to_redshift] >> \
    load_songplays_table >> [load_user_dimension_table, load_song_dimension_table, load_artist_dimension_table, load_time_dimension_table] >> \
    run_quality_checks >> end_operator

final_project_dag = final_project()
