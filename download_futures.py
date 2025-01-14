import databento as db

client = db.Historical("db-raWg8w766GAKLDXRc63fjwQ9qiY88")

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["SR3Z5"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/SR3Z5.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["SR3U5"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/SR3U5.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["SR3M5"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/SR3M5.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["SR3H5"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/SR3H5.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["SR3Z4"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/SR3Z4.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["SR3U4"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/SR3U4.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["SR3M4"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/SR3M4.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["SR3H4"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/SR3H4.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["SR3Z3"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/SR3Z3.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["SR3U3"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/SR3U3.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["SR3M3"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/SR3M3.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["SR3H3"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/SR3H3.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["SR3Z2"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/SR3Z2.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["SR3U2"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/SR3U2.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["SR3M2"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/SR3M2.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["SR3H2"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/SR3H2.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEZ3"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEZ3.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEU3"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEU3.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEM3"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEM3.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEH3"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEH3.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEZ2"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEZ2.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEU2"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEU2.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEM2"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEM2.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEH2"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEH2.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEZ1"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEZ1.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEU1"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEU1.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEM1"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEM1.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEH1"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEH1.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEZ0"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEZ0.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEU0"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEU0.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEM0"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEM0.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEH0"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEH0.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEZ9"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEZ9.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEU9"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEU9.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEM9"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEM9.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEH9"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEH9.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEZ8"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEZ8.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEU8"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEU8.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEM8"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEM8.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEH8"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEH8.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEZ7"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEZ7.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEU7"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEU7.csv')

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    # symbols=["ZQQ4"],
    symbols=["GEM7"],
    schema="ohlcv-1m",
    start="2017-05-21T14:20:00",
    end="2024-08-17T00:00:00",
)
df = data.to_df()
df.to_csv('D:/AA econ/research track/data/futures/GEM7.csv')



# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESU4"],
#     schema="ohlcv-1m",
#     start="2023-01-03T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESU4.csv')

# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESM4"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESM4.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESH4"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESH4.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESZ3"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESZ3.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESU3"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESU3.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESM3"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESM3.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESH3"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESH3.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESZ2"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESZ2.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESU2"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESU2.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESM2"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESM2.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESH2"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESH2.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESZ1"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESZ1.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESU1"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESU1.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESM1"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESM1.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESH1"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESH1.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESZ0"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESZ0.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESU0"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESU0.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESM0"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESM0.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESH0"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESH0.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESZ9"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESZ9.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESU9"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESU9.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESM9"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESM9.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESH9"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESH9.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESZ8"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESZ8.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESU8"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESU8.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESM8"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESM8.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESH8"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESH8.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESZ7"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESZ7.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESU7"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESU7.csv')
#
# data = client.timeseries.get_range(
#     dataset="GLBX.MDP3",
#     # symbols=["ZQQ4"],
#     symbols=["ESM7"],
#     schema="ohlcv-1m",
#     start="2017-05-21T14:20:00",
#     end="2024-08-17T00:00:00",
# )
# df = data.to_df()
# df.to_csv('D:/AA econ/research track/data/futures/ESM7.csv')


# data = client.timeseries.get_range(
#     dataset='GLBX.MDP3',
#     symbols='ES.FUT',
#     stype_in='parent',
#     start='2022-06-10T14:30',
#     end='2022-06-10T14:40',
# )
#
# data.replay(callback=print)
