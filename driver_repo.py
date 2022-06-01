from datetime import timedelta

#from feast import FileSource, Entity, Feature, FeatureView, ValueType
from feast import Entity, FeatureView, Field, FileSource, ValueType
from feast.types import Float32, Int64
driver = Entity(name="driver_id", join_key="driver_id", value_type=ValueType.INT64,)

driver_stats_source = FileSource(
    path="data/driver_stats.parquet",
    event_timestamp_column="event_timestamp",
    created_timestamp_column="created",
)

driver_stats_fv = FeatureView(
    name="driver_hourly_stats",
    entities=["driver_id"],
    ttl=timedelta(weeks=52),
    schema=[
        Field(name="conv_rate", dtype=Float32),
        Field(name="acc_rate", dtype=Float32),
        Field(name="avg_daily_trips", dtype=Int64),
    ],
    batch_source=driver_stats_source,
    tags={"team": "driver_performance"},
    online=True
)
