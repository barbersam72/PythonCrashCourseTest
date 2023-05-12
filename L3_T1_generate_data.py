
import random
import shutil
import os

data_dir = 'data'

# Remove old data dir if it exists
if os.path.isdir(data_dir):
	shutil.rmtree(data_dir)

# Make a new data dir
os.mkdir(data_dir)

file_list = ["HL_fri_nov_25_00:04:15_2016_033253.eps.png", "HL_fri_nov_25_00:15:51_2016_468285.eps.png", "HL_fri_nov_25_00:26:07_2016_424044.eps.png", "HL_fri_nov_25_00:36:19_2016_014794.eps.png", "HL_fri_nov_25_00:46:31_2016_301042.eps.png", "HL_fri_nov_25_00:58:33_2016_576374.eps.png", "HL_fri_nov_25_01:09:50_2016_171095.eps.png", "HL_fri_nov_25_01:21:27_2016_821116.eps.png", "HL_fri_nov_25_01:31:59_2016_210636.eps.png", "HL_fri_nov_25_01:43:01_2016_024221.eps.png", "HL_fri_nov_25_01:56:17_2016_163561.eps.png", "HL_fri_nov_25_02:06:57_2016_600605.eps.png", "HL_fri_nov_25_02:17:26_2016_856217.eps.png", "HL_fri_nov_25_02:27:54_2016_370336.eps.png", "HL_fri_nov_25_02:39:09_2016_575070.eps.png", "HL_fri_nov_25_02:49:19_2016_052853.eps.png", "HL_fri_nov_25_03:00:31_2016_774194.eps.png", "HL_fri_nov_25_03:11:05_2016_818719.eps.png", "HL_fri_nov_25_03:22:49_2016_341189.eps.png", "HL_fri_nov_25_03:33:46_2016_173341.eps.png", "HL_fri_nov_25_03:46:28_2016_387774.eps.png", "HL_fri_nov_25_03:56:57_2016_160876.eps.png", "HL_fri_nov_25_04:09:13_2016_574495.eps.png", "HL_fri_nov_25_04:19:23_2016_574824.eps.png", "HL_fri_nov_25_04:29:34_2016_357810.eps.png", "HL_fri_nov_25_04:39:49_2016_892939.eps.png", "HL_fri_nov_25_04:50:16_2016_922411.eps.png", "HL_fri_nov_25_05:00:28_2016_174272.eps.png", "HL_fri_nov_25_05:10:44_2016_010048.eps.png", "HL_fri_nov_25_05:20:55_2016_476824.eps.png", "HL_fri_nov_25_05:33:15_2016_576613.eps.png", "HL_fri_nov_25_05:44:05_2016_853479.eps.png", "HL_fri_nov_25_05:56:32_2016_457130.eps.png", "HL_fri_nov_25_06:06:56_2016_509904.eps.png", "HL_fri_nov_25_06:17:16_2016_982551.eps.png", "HL_fri_nov_25_06:28:03_2016_122523.eps.png", "HL_fri_nov_25_06:39:30_2016_231969.eps.png", "HL_fri_nov_25_06:49:51_2016_158985.eps.png", "HL_fri_nov_25_07:01:51_2016_202519.eps.png", "HL_fri_nov_25_07:12:59_2016_931034.eps.png", "HL_fri_nov_25_07:24:21_2016_185496.eps.png", "HL_fri_nov_25_07:36:55_2016_357616.eps.png", "HL_fri_nov_25_07:48:35_2016_984875.eps.png", "HL_fri_nov_25_08:00:06_2016_920938.eps.png", "HL_fri_nov_25_08:10:13_2016_202902.eps.png", "HL_fri_nov_25_08:20:49_2016_488350.eps.png", "HL_fri_nov_25_08:32:46_2016_597395.eps.png", "HL_fri_nov_25_08:45:32_2016_420212.eps.png", "HL_fri_nov_25_08:56:03_2016_762341.eps.png", "HL_fri_nov_25_09:06:39_2016_155739.eps.png", "HL_fri_nov_25_09:17:08_2016_716355.eps.png", "HL_fri_nov_25_09:27:22_2016_528766.eps.png", "HL_fri_nov_25_09:38:04_2016_171726.eps.png", "HL_fri_nov_25_09:48:20_2016_406291.eps.png", "HL_fri_nov_25_09:58:34_2016_609739.eps.png", "HL_fri_nov_25_10:09:15_2016_234176.eps.png", "HL_fri_nov_25_10:20:10_2016_417699.eps.png", "HL_fri_nov_25_10:31:12_2016_233430.eps.png", "HL_fri_nov_25_10:41:36_2016_214235.eps.png", "HL_fri_nov_25_10:51:45_2016_106601.eps.png", "HL_fri_nov_25_11:02:14_2016_132869.eps.png", "HL_fri_nov_25_11:13:44_2016_894160.eps.png", "HL_fri_nov_25_11:23:58_2016_343611.eps.png", "HL_fri_nov_25_11:34:10_2016_528914.eps.png", "HL_fri_nov_25_11:46:04_2016_411380.eps.png", "HL_fri_nov_25_11:57:16_2016_267828.eps.png", "HL_fri_nov_25_12:08:25_2016_844841.eps.png", "HL_fri_nov_25_12:19:28_2016_935048.eps.png", "HL_fri_nov_25_12:31:35_2016_444374.eps.png", "HL_fri_nov_25_12:42:23_2016_505704.eps.png", "HL_fri_nov_25_12:52:34_2016_640087.eps.png", "HL_fri_nov_25_13:04:09_2016_880599.eps.png", "HL_fri_nov_25_13:14:18_2016_783008.eps.png", "HL_fri_nov_25_13:24:41_2016_189429.eps.png", "HL_fri_nov_25_13:35:49_2016_462911.eps.png", "HL_fri_nov_25_13:47:56_2016_239200.eps.png", "HL_fri_nov_25_13:58:51_2016_527288.eps.png", "HL_fri_nov_25_14:09:24_2016_720131.eps.png", "HL_fri_nov_25_14:19:46_2016_044152.eps.png", "HL_fri_nov_25_14:30:19_2016_503202.eps.png", "HL_fri_nov_25_14:40:35_2016_007314.eps.png", "HL_fri_nov_25_14:50:45_2016_501117.eps.png", "HL_fri_nov_25_15:01:19_2016_962726.eps.png", "HL_fri_nov_25_15:11:57_2016_065410.eps.png", "HL_fri_nov_25_15:22:11_2016_335065.eps.png", "HL_fri_nov_25_15:32:58_2016_759901.eps.png", "HL_fri_nov_25_15:43:09_2016_221333.eps.png", "HL_fri_nov_25_15:55:12_2016_598676.eps.png", "HL_fri_nov_25_16:05:51_2016_987360.eps.png", "HL_fri_nov_25_16:17:02_2016_889378.eps.png", "HL_fri_nov_25_16:28:27_2016_796607.eps.png", "HL_fri_nov_25_16:38:53_2016_410227.eps.png", "HL_fri_nov_25_16:49:27_2016_099227.eps.png", "HL_fri_nov_25_17:01:43_2016_147595.eps.png", "HL_fri_nov_25_17:11:57_2016_187190.eps.png", "HL_fri_nov_25_17:22:21_2016_624519.eps.png", "HL_fri_nov_25_17:33:15_2016_832765.eps.png", "HL_fri_nov_25_17:43:40_2016_605550.eps.png", "HL_fri_nov_25_17:54:01_2016_441824.eps.png", "HL_fri_nov_25_18:04:30_2016_766140.eps.png", "HL_fri_nov_25_18:16:52_2016_694904.eps.png", "HL_fri_nov_25_18:27:20_2016_067088.eps.png", "HL_fri_nov_25_18:37:34_2016_944711.eps.png", "HL_fri_nov_25_18:48:31_2016_216136.eps.png", "HL_fri_nov_25_18:59:16_2016_966726.eps.png", "HL_fri_nov_25_19:09:39_2016_879734.eps.png", "HL_fri_nov_25_19:20:12_2016_452307.eps.png", "HL_fri_nov_25_19:30:24_2016_072912.eps.png", "HL_fri_nov_25_19:41:01_2016_961595.eps.png", "HL_fri_nov_25_19:51:45_2016_094113.eps.png", "HL_fri_nov_25_20:04:21_2016_851437.eps.png", "HL_fri_nov_25_20:14:38_2016_244804.eps.png", "HL_fri_nov_25_20:25:05_2016_194138.eps.png", "HL_fri_nov_25_20:35:30_2016_706584.eps.png", "HL_fri_nov_25_20:46:18_2016_115551.eps.png", "HL_fri_nov_25_20:56:51_2016_434613.eps.png", "HL_fri_nov_25_21:07:16_2016_345802.eps.png", "HL_fri_nov_25_21:19:39_2016_242295.eps.png", "HL_fri_nov_25_21:29:56_2016_073324.eps.png", "HL_fri_nov_25_21:40:57_2016_912744.eps.png", "HL_fri_nov_25_21:51:21_2016_811232.eps.png", "HL_fri_nov_25_22:02:00_2016_464853.eps.png", "HL_fri_nov_25_22:12:33_2016_311646.eps.png", "HL_fri_nov_25_22:23:06_2016_419059.eps.png", "HL_fri_nov_25_22:33:21_2016_300501.eps.png", "HL_fri_nov_25_22:43:42_2016_578129.eps.png", "HL_fri_nov_25_22:54:12_2016_329028.eps.png", "HL_fri_nov_25_23:04:26_2016_740298.eps.png", "HL_fri_nov_25_23:15:14_2016_256177.eps.png", "HL_fri_nov_25_23:25:58_2016_916026.eps.png", "HL_fri_nov_25_23:36:37_2016_105106.eps.png", "HL_fri_nov_25_23:47:07_2016_939296.eps.png", "HL_fri_nov_25_23:57:19_2016_072604.eps.png", "HL_sat_nov_26_00:07:34_2016_938694.eps.png", "HL_sat_nov_26_00:18:51_2016_373893.eps.png", "HL_sat_nov_26_00:30:12_2016_179003.eps.png", "HL_sat_nov_26_00:41:09_2016_322502.eps.png", "HL_sat_nov_26_00:51:24_2016_672569.eps.png", "HL_sat_nov_26_01:02:44_2016_255697.eps.png", "HL_sat_nov_26_01:13:03_2016_724490.eps.png", "HL_sat_nov_26_01:23:18_2016_026832.eps.png", "HL_sat_nov_26_01:34:57_2016_831493.eps.png", "HL_sat_nov_26_01:45:58_2016_192203.eps.png", "HL_sat_nov_26_01:56:16_2016_804459.eps.png", "HL_sat_nov_26_02:06:36_2016_858523.eps.png", "HL_sat_nov_26_02:16:50_2016_655082.eps.png", "HL_sat_nov_26_02:27:08_2016_857223.eps.png", "HL_sat_nov_26_02:38:04_2016_438484.eps.png", "HL_sat_nov_26_02:49:52_2016_887962.eps.png", "HL_sat_nov_26_03:00:16_2016_902515.eps.png", "HL_sat_nov_26_03:12:51_2016_496125.eps.png", "HL_sat_nov_26_03:24:34_2016_026536.eps.png", "HL_sat_nov_26_03:35:00_2016_657004.eps.png", "HL_sat_nov_26_03:46:26_2016_520036.eps.png", "HL_sat_nov_26_03:57:18_2016_046552.eps.png", "HL_sat_nov_26_04:07:50_2016_890097.eps.png", "HL_sat_nov_26_04:18:04_2016_516449.eps.png", "HL_sat_nov_26_04:28:16_2016_351240.eps.png", "HL_sat_nov_26_04:39:16_2016_989250.eps.png", "HL_sat_nov_26_04:50:18_2016_660016.eps.png", "HL_sat_nov_26_05:00:42_2016_849595.eps.png", "HL_sat_nov_26_05:10:54_2016_769435.eps.png", "HL_sat_nov_26_05:22:22_2016_029131.eps.png", "HL_sat_nov_26_05:32:36_2016_736873.eps.png", "HL_sat_nov_26_05:42:58_2016_330729.eps.png", "HL_sat_nov_26_05:54:02_2016_615680.eps.png", "HL_sat_nov_26_06:05:04_2016_134961.eps.png", "HL_sat_nov_26_06:15:57_2016_240059.eps.png", "HL_sat_nov_26_06:26:21_2016_647349.eps.png", "HL_sat_nov_26_06:37:08_2016_089369.eps.png", "HL_sat_nov_26_06:47:52_2016_174835.eps.png", "HL_sat_nov_26_06:58:30_2016_241191.eps.png", "HL_sat_nov_26_07:08:58_2016_214702.eps.png", "HL_sat_nov_26_07:20:19_2016_246337.eps.png", "HL_sat_nov_26_07:30:38_2016_143436.eps.png", "HL_sat_nov_26_07:41:28_2016_712853.eps.png", "HL_thu_nov_24_17:36:09_2016_444276.eps.png", "HL_thu_nov_24_17:46:23_2016_731160.eps.png", "HL_thu_nov_24_17:57:18_2016_837572.eps.png", "HL_thu_nov_24_18:08:11_2016_892297.eps.png", "HL_thu_nov_24_18:19:42_2016_682931.eps.png", "HL_thu_nov_24_18:30:04_2016_566493.eps.png", "HL_thu_nov_24_18:41:40_2016_671701.eps.png", "HL_thu_nov_24_18:51:55_2016_914777.eps.png", "HL_thu_nov_24_19:03:14_2016_882919.eps.png", "HL_thu_nov_24_19:14:43_2016_437752.eps.png", "HL_thu_nov_24_19:25:08_2016_639806.eps.png", "HL_thu_nov_24_19:36:56_2016_110029.eps.png", "HL_thu_nov_24_19:48:09_2016_553224.eps.png", "HL_thu_nov_24_19:58:21_2016_957621.eps.png", "HL_thu_nov_24_20:08:42_2016_728432.eps.png", "HL_thu_nov_24_20:19:14_2016_537977.eps.png", "HL_thu_nov_24_20:29:26_2016_555749.eps.png", "HL_thu_nov_24_20:39:40_2016_985386.eps.png", "HL_thu_nov_24_20:49:53_2016_928033.eps.png", "HL_thu_nov_24_21:00:29_2016_335098.eps.png", "HL_thu_nov_24_21:11:21_2016_453752.eps.png", "HL_thu_nov_24_21:21:49_2016_404198.eps.png", "HL_thu_nov_24_21:32:22_2016_762083.eps.png", "HL_thu_nov_24_21:44:50_2016_806726.eps.png", "HL_thu_nov_24_21:55:47_2016_394538.eps.png", "HL_thu_nov_24_22:06:37_2016_795404.eps.png", "HL_thu_nov_24_22:17:33_2016_841514.eps.png", "HL_thu_nov_24_22:28:30_2016_456407.eps.png", "HL_thu_nov_24_22:39:00_2016_901124.eps.png", "HL_thu_nov_24_22:49:55_2016_774323.eps.png", "HL_thu_nov_24_23:01:03_2016_418641.eps.png", "HL_thu_nov_24_23:11:42_2016_215622.eps.png", "HL_thu_nov_24_23:22:12_2016_865827.eps.png", "HL_thu_nov_24_23:32:29_2016_042069.eps.png", "HL_thu_nov_24_23:42:38_2016_611111.eps.png", "HL_thu_nov_24_23:52:47_2016_385398.eps.png"]

# Generate files

for file_name in file_list:

	file_name = file_name.replace(':', '-') + '.txt'
	with open(os.path.join(data_dir, file_name), 'w') as f:
		f.write(str(random.random()))
