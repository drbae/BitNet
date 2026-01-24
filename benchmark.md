# Benchmark Results

| model                                   |       size |     params | backend    | threads | n_batch |          test |                  t/s |
| --------------------------------------- | ---------: | ---------: | ---------- | ------: | ------: | ------------: | -------------------: |
| bitnet-b1.58 2B I2_S - 2 bpw ternary    |   1.71 GiB |     2.74 B | CPU        |      24 |       1 |        pp2560 |         23.55 ± 0.14 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary    |   1.71 GiB |     2.74 B | CPU        |      24 |       1 |        tg2000 |         24.75 ± 0.20 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary    |   1.71 GiB |     2.74 B | CPU        |      24 |       1 |         pp256 |         26.37 ± 1.03 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary    |   1.71 GiB |     2.74 B | CPU        |      24 |       1 |         tg200 |         26.92 ± 0.62 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary    |   1.71 GiB |     2.74 B | CPU        |      12 |       1 |         pp256 |         29.53 ± 0.42 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary    |   1.71 GiB |     2.74 B | CPU        |      12 |       1 |         tg200 |         29.95 ± 0.43 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary    |   1.71 GiB |     2.74 B | CPU        |       6 |       1 |         pp256 |         30.73 ± 0.21 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary    |   1.71 GiB |     2.74 B | CPU        |       6 |       1 |         tg200 |         30.87 ± 0.21 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary    |   1.71 GiB |     2.74 B | CPU        |       4 |       1 |         pp256 |         27.42 ± 0.19 |
| bitnet-b1.58 2B I2_S - 2 bpw ternary    |   1.71 GiB |     2.74 B | CPU        |       4 |       1 |         tg200 |         27.02 ± 0.47 |
