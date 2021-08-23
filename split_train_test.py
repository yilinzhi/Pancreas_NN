# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2021/08/20 11:38
# @Author  : Yi
# @FileName: split_train_test.py

"""
    TODO：
        数据来源：https://github.com/JunMa11/SegLoss/tree/master/test，包含NIH和MSD两块数据，一共363个数据。
        测试集的划分依据：https://zenodo.org/record/4738480#.YR8YeY4zZdg，73个数据集。
        steps:
            划分出test_file_name,然后从imagesTr/labelsTr移出到imagesTs/labelsTr
            对Task002_pancreas重命名Task503_pancreas
            修改dataset.json文件内容
"""

import os

test_path = r"E:\Medical_Image_Research\Segmentation_Project\nnUNetFrame\Datasets\Task503_Test\GroundTruth\Task002_Pancreas"
test_file_name = os.listdir(test_path)
test_id = []
for file_name in test_file_name:
    id = file_name[9:12]
    test_id.append(id)

train_path = r"E:\Medical_Image_Research\Segmentation_Project\nnUNetFrame\Datasets\Task503_Pancreas\imagesTr"
train_file_name = os.listdir(train_path)
train_id = []
for file_name in train_file_name:
    id = file_name[9:12]
    train_id.append(id)

train_set = list(set(train_id) - set(test_id))

print(len(test_id))
print(len(train_id))
print(len(train_set))
print(test_id)
print(train_set)

ts_id = ['021', '024', '040', '041', '042', '045', '051', '058', '067', '071', '075', '077', '087', '089', '092', '095',
         '110', '119', '138', '145', '147', '166', '169', '170', '175', '180', '186', '191', '193', '194', '213', '222',
         '225', '226', '235', '256', '261', '284', '286', '290', '294', '299', '305', '312', '315', '320', '336', '343',
         '364', '367', '370', '372', '385', '386', '398', '401', '411', '415', '422', '423', '425', '436', '441', '442',
         '444', '446', '466', '476', '485', '487', '490', '494', '502']

true_train = []
true_test = []
for file_name in train_file_name:
    id = file_name[9:12]
    if id in ts_id:
        true_test.append(file_name)
    else:
        true_train.append(file_name)

print(len(true_train))
print(len(true_test))
print(true_train)
print(true_test)

test = ['pancreas_021_0000.nii.gz', 'pancreas_024_0000.nii.gz', 'pancreas_040_0000.nii.gz', 'pancreas_041_0000.nii.gz',
        'pancreas_042_0000.nii.gz', 'pancreas_045_0000.nii.gz', 'pancreas_051_0000.nii.gz', 'pancreas_058_0000.nii.gz',
        'pancreas_067_0000.nii.gz', 'pancreas_071_0000.nii.gz', 'pancreas_075_0000.nii.gz', 'pancreas_077_0000.nii.gz',
        'pancreas_087_0000.nii.gz', 'pancreas_089_0000.nii.gz', 'pancreas_092_0000.nii.gz', 'pancreas_095_0000.nii.gz',
        'pancreas_110_0000.nii.gz', 'pancreas_119_0000.nii.gz', 'pancreas_138_0000.nii.gz', 'pancreas_145_0000.nii.gz',
        'pancreas_147_0000.nii.gz', 'pancreas_166_0000.nii.gz', 'pancreas_169_0000.nii.gz', 'pancreas_170_0000.nii.gz',
        'pancreas_175_0000.nii.gz', 'pancreas_180_0000.nii.gz', 'pancreas_186_0000.nii.gz', 'pancreas_191_0000.nii.gz',
        'pancreas_193_0000.nii.gz', 'pancreas_194_0000.nii.gz', 'pancreas_213_0000.nii.gz', 'pancreas_222_0000.nii.gz',
        'pancreas_225_0000.nii.gz', 'pancreas_226_0000.nii.gz', 'pancreas_235_0000.nii.gz', 'pancreas_256_0000.nii.gz',
        'pancreas_261_0000.nii.gz', 'pancreas_284_0000.nii.gz', 'pancreas_286_0000.nii.gz', 'pancreas_290_0000.nii.gz',
        'pancreas_294_0000.nii.gz', 'pancreas_299_0000.nii.gz', 'pancreas_305_0000.nii.gz', 'pancreas_312_0000.nii.gz',
        'pancreas_315_0000.nii.gz', 'pancreas_320_0000.nii.gz', 'pancreas_336_0000.nii.gz', 'pancreas_343_0000.nii.gz',
        'pancreas_364_0000.nii.gz', 'pancreas_367_0000.nii.gz', 'pancreas_370_0000.nii.gz', 'pancreas_372_0000.nii.gz',
        'pancreas_385_0000.nii.gz', 'pancreas_386_0000.nii.gz', 'pancreas_398_0000.nii.gz', 'pancreas_401_0000.nii.gz',
        'pancreas_411_0000.nii.gz', 'pancreas_415_0000.nii.gz', 'pancreas_422_0000.nii.gz', 'pancreas_423_0000.nii.gz',
        'pancreas_425_0000.nii.gz', 'pancreas_436_0000.nii.gz', 'pancreas_441_0000.nii.gz', 'pancreas_442_0000.nii.gz',
        'pancreas_444_0000.nii.gz', 'pancreas_446_0000.nii.gz', 'pancreas_466_0000.nii.gz', 'pancreas_476_0000.nii.gz',
        'pancreas_485_0000.nii.gz', 'pancreas_487_0000.nii.gz', 'pancreas_490_0000.nii.gz', 'pancreas_494_0000.nii.gz',
        'pancreas_502_0000.nii.gz']
train = ['pancreas_001_0000.nii.gz', 'pancreas_004_0000.nii.gz', 'pancreas_005_0000.nii.gz', 'pancreas_006_0000.nii.gz',
         'pancreas_010_0000.nii.gz', 'pancreas_012_0000.nii.gz', 'pancreas_015_0000.nii.gz', 'pancreas_016_0000.nii.gz',
         'pancreas_018_0000.nii.gz', 'pancreas_019_0000.nii.gz', 'pancreas_025_0000.nii.gz', 'pancreas_028_0000.nii.gz',
         'pancreas_029_0000.nii.gz', 'pancreas_032_0000.nii.gz', 'pancreas_035_0000.nii.gz', 'pancreas_037_0000.nii.gz',
         'pancreas_043_0000.nii.gz', 'pancreas_046_0000.nii.gz', 'pancreas_048_0000.nii.gz', 'pancreas_049_0000.nii.gz',
         'pancreas_050_0000.nii.gz', 'pancreas_052_0000.nii.gz', 'pancreas_055_0000.nii.gz', 'pancreas_056_0000.nii.gz',
         'pancreas_061_0000.nii.gz', 'pancreas_064_0000.nii.gz', 'pancreas_066_0000.nii.gz', 'pancreas_069_0000.nii.gz',
         'pancreas_070_0000.nii.gz', 'pancreas_074_0000.nii.gz', 'pancreas_078_0000.nii.gz', 'pancreas_080_0000.nii.gz',
         'pancreas_081_0000.nii.gz', 'pancreas_083_0000.nii.gz', 'pancreas_084_0000.nii.gz', 'pancreas_086_0000.nii.gz',
         'pancreas_088_0000.nii.gz', 'pancreas_091_0000.nii.gz', 'pancreas_093_0000.nii.gz', 'pancreas_094_0000.nii.gz',
         'pancreas_096_0000.nii.gz', 'pancreas_098_0000.nii.gz', 'pancreas_099_0000.nii.gz', 'pancreas_100_0000.nii.gz',
         'pancreas_101_0000.nii.gz', 'pancreas_102_0000.nii.gz', 'pancreas_103_0000.nii.gz', 'pancreas_104_0000.nii.gz',
         'pancreas_105_0000.nii.gz', 'pancreas_106_0000.nii.gz', 'pancreas_107_0000.nii.gz', 'pancreas_109_0000.nii.gz',
         'pancreas_111_0000.nii.gz', 'pancreas_113_0000.nii.gz', 'pancreas_114_0000.nii.gz', 'pancreas_117_0000.nii.gz',
         'pancreas_120_0000.nii.gz', 'pancreas_122_0000.nii.gz', 'pancreas_124_0000.nii.gz', 'pancreas_125_0000.nii.gz',
         'pancreas_126_0000.nii.gz', 'pancreas_127_0000.nii.gz', 'pancreas_129_0000.nii.gz', 'pancreas_130_0000.nii.gz',
         'pancreas_131_0000.nii.gz', 'pancreas_135_0000.nii.gz', 'pancreas_137_0000.nii.gz', 'pancreas_140_0000.nii.gz',
         'pancreas_148_0000.nii.gz', 'pancreas_149_0000.nii.gz', 'pancreas_155_0000.nii.gz', 'pancreas_157_0000.nii.gz',
         'pancreas_158_0000.nii.gz', 'pancreas_159_0000.nii.gz', 'pancreas_160_0000.nii.gz', 'pancreas_165_0000.nii.gz',
         'pancreas_167_0000.nii.gz', 'pancreas_172_0000.nii.gz', 'pancreas_173_0000.nii.gz', 'pancreas_178_0000.nii.gz',
         'pancreas_179_0000.nii.gz', 'pancreas_181_0000.nii.gz', 'pancreas_182_0000.nii.gz', 'pancreas_183_0000.nii.gz',
         'pancreas_187_0000.nii.gz', 'pancreas_196_0000.nii.gz', 'pancreas_197_0000.nii.gz', 'pancreas_198_0000.nii.gz',
         'pancreas_199_0000.nii.gz', 'pancreas_200_0000.nii.gz', 'pancreas_201_0000.nii.gz', 'pancreas_203_0000.nii.gz',
         'pancreas_204_0000.nii.gz', 'pancreas_207_0000.nii.gz', 'pancreas_209_0000.nii.gz', 'pancreas_210_0000.nii.gz',
         'pancreas_211_0000.nii.gz', 'pancreas_212_0000.nii.gz', 'pancreas_214_0000.nii.gz', 'pancreas_215_0000.nii.gz',
         'pancreas_217_0000.nii.gz', 'pancreas_218_0000.nii.gz', 'pancreas_219_0000.nii.gz', 'pancreas_224_0000.nii.gz',
         'pancreas_227_0000.nii.gz', 'pancreas_228_0000.nii.gz', 'pancreas_229_0000.nii.gz', 'pancreas_230_0000.nii.gz',
         'pancreas_231_0000.nii.gz', 'pancreas_234_0000.nii.gz', 'pancreas_236_0000.nii.gz', 'pancreas_239_0000.nii.gz',
         'pancreas_241_0000.nii.gz', 'pancreas_242_0000.nii.gz', 'pancreas_243_0000.nii.gz', 'pancreas_244_0000.nii.gz',
         'pancreas_246_0000.nii.gz', 'pancreas_247_0000.nii.gz', 'pancreas_249_0000.nii.gz', 'pancreas_253_0000.nii.gz',
         'pancreas_254_0000.nii.gz', 'pancreas_255_0000.nii.gz', 'pancreas_258_0000.nii.gz', 'pancreas_259_0000.nii.gz',
         'pancreas_262_0000.nii.gz', 'pancreas_264_0000.nii.gz', 'pancreas_265_0000.nii.gz', 'pancreas_266_0000.nii.gz',
         'pancreas_267_0000.nii.gz', 'pancreas_268_0000.nii.gz', 'pancreas_269_0000.nii.gz', 'pancreas_270_0000.nii.gz',
         'pancreas_274_0000.nii.gz', 'pancreas_275_0000.nii.gz', 'pancreas_276_0000.nii.gz', 'pancreas_277_0000.nii.gz',
         'pancreas_278_0000.nii.gz', 'pancreas_279_0000.nii.gz', 'pancreas_280_0000.nii.gz', 'pancreas_283_0000.nii.gz',
         'pancreas_285_0000.nii.gz', 'pancreas_287_0000.nii.gz', 'pancreas_289_0000.nii.gz', 'pancreas_291_0000.nii.gz',
         'pancreas_292_0000.nii.gz', 'pancreas_293_0000.nii.gz', 'pancreas_295_0000.nii.gz', 'pancreas_296_0000.nii.gz',
         'pancreas_297_0000.nii.gz', 'pancreas_298_0000.nii.gz', 'pancreas_300_0000.nii.gz', 'pancreas_301_0000.nii.gz',
         'pancreas_302_0000.nii.gz', 'pancreas_303_0000.nii.gz', 'pancreas_304_0000.nii.gz', 'pancreas_308_0000.nii.gz',
         'pancreas_309_0000.nii.gz', 'pancreas_310_0000.nii.gz', 'pancreas_311_0000.nii.gz', 'pancreas_313_0000.nii.gz',
         'pancreas_316_0000.nii.gz', 'pancreas_318_0000.nii.gz', 'pancreas_321_0000.nii.gz', 'pancreas_323_0000.nii.gz',
         'pancreas_325_0000.nii.gz', 'pancreas_326_0000.nii.gz', 'pancreas_327_0000.nii.gz', 'pancreas_328_0000.nii.gz',
         'pancreas_329_0000.nii.gz', 'pancreas_330_0000.nii.gz', 'pancreas_331_0000.nii.gz', 'pancreas_333_0000.nii.gz',
         'pancreas_334_0000.nii.gz', 'pancreas_339_0000.nii.gz', 'pancreas_342_0000.nii.gz', 'pancreas_344_0000.nii.gz',
         'pancreas_345_0000.nii.gz', 'pancreas_346_0000.nii.gz', 'pancreas_347_0000.nii.gz', 'pancreas_348_0000.nii.gz',
         'pancreas_350_0000.nii.gz', 'pancreas_351_0000.nii.gz', 'pancreas_354_0000.nii.gz', 'pancreas_355_0000.nii.gz',
         'pancreas_356_0000.nii.gz', 'pancreas_357_0000.nii.gz', 'pancreas_358_0000.nii.gz', 'pancreas_360_0000.nii.gz',
         'pancreas_361_0000.nii.gz', 'pancreas_362_0000.nii.gz', 'pancreas_365_0000.nii.gz', 'pancreas_366_0000.nii.gz',
         'pancreas_369_0000.nii.gz', 'pancreas_374_0000.nii.gz', 'pancreas_375_0000.nii.gz', 'pancreas_376_0000.nii.gz',
         'pancreas_377_0000.nii.gz', 'pancreas_378_0000.nii.gz', 'pancreas_379_0000.nii.gz', 'pancreas_380_0000.nii.gz',
         'pancreas_382_0000.nii.gz', 'pancreas_387_0000.nii.gz', 'pancreas_388_0000.nii.gz', 'pancreas_389_0000.nii.gz',
         'pancreas_391_0000.nii.gz', 'pancreas_392_0000.nii.gz', 'pancreas_393_0000.nii.gz', 'pancreas_395_0000.nii.gz',
         'pancreas_399_0000.nii.gz', 'pancreas_400_0000.nii.gz', 'pancreas_402_0000.nii.gz', 'pancreas_404_0000.nii.gz',
         'pancreas_405_0000.nii.gz', 'pancreas_406_0000.nii.gz', 'pancreas_409_0000.nii.gz', 'pancreas_410_0000.nii.gz',
         'pancreas_412_0000.nii.gz', 'pancreas_413_0000.nii.gz', 'pancreas_414_0000.nii.gz', 'pancreas_416_0000.nii.gz',
         'pancreas_418_0000.nii.gz', 'pancreas_419_0000.nii.gz', 'pancreas_421_0000.nii.gz', 'pancreas_424_0000.nii.gz',
         'pancreas_426_0000.nii.gz', 'pancreas_427_0000.nii.gz', 'pancreas_428_0000.nii.gz', 'pancreas_429_0000.nii.gz',
         'pancreas_430_0000.nii.gz', 'pancreas_431_0000.nii.gz', 'pancreas_432_0000.nii.gz', 'pancreas_433_0000.nii.gz',
         'pancreas_434_0000.nii.gz', 'pancreas_435_0000.nii.gz', 'pancreas_437_0000.nii.gz', 'pancreas_438_0000.nii.gz',
         'pancreas_439_0000.nii.gz', 'pancreas_440_0000.nii.gz', 'pancreas_443_0000.nii.gz', 'pancreas_445_0000.nii.gz',
         'pancreas_447_0000.nii.gz', 'pancreas_448_0000.nii.gz', 'pancreas_449_0000.nii.gz', 'pancreas_450_0000.nii.gz',
         'pancreas_451_0000.nii.gz', 'pancreas_452_0000.nii.gz', 'pancreas_453_0000.nii.gz', 'pancreas_454_0000.nii.gz',
         'pancreas_455_0000.nii.gz', 'pancreas_456_0000.nii.gz', 'pancreas_457_0000.nii.gz', 'pancreas_458_0000.nii.gz',
         'pancreas_459_0000.nii.gz', 'pancreas_460_0000.nii.gz', 'pancreas_461_0000.nii.gz', 'pancreas_462_0000.nii.gz',
         'pancreas_463_0000.nii.gz', 'pancreas_464_0000.nii.gz', 'pancreas_465_0000.nii.gz', 'pancreas_467_0000.nii.gz',
         'pancreas_468_0000.nii.gz', 'pancreas_469_0000.nii.gz', 'pancreas_470_0000.nii.gz', 'pancreas_471_0000.nii.gz',
         'pancreas_472_0000.nii.gz', 'pancreas_473_0000.nii.gz', 'pancreas_474_0000.nii.gz', 'pancreas_475_0000.nii.gz',
         'pancreas_477_0000.nii.gz', 'pancreas_478_0000.nii.gz', 'pancreas_479_0000.nii.gz', 'pancreas_480_0000.nii.gz',
         'pancreas_481_0000.nii.gz', 'pancreas_482_0000.nii.gz', 'pancreas_483_0000.nii.gz', 'pancreas_484_0000.nii.gz',
         'pancreas_486_0000.nii.gz', 'pancreas_488_0000.nii.gz', 'pancreas_489_0000.nii.gz', 'pancreas_491_0000.nii.gz',
         'pancreas_492_0000.nii.gz', 'pancreas_493_0000.nii.gz', 'pancreas_495_0000.nii.gz', 'pancreas_496_0000.nii.gz',
         'pancreas_497_0000.nii.gz', 'pancreas_498_0000.nii.gz', 'pancreas_499_0000.nii.gz', 'pancreas_500_0000.nii.gz',
         'pancreas_501_0000.nii.gz', 'pancreas_503_0000.nii.gz']

train_label_path = r'E:\Medical_Image_Research\Segmentation_Project\nnUNetFrame\Datasets\Task503_Pancreas\labelsTr'
train_label_file = os.listdir(train_label_path)

true_train_label = []
true_test_label = []
for file_name in train_label_file:
    id = file_name[9:12]
    if id in ts_id:
        true_test_label.append(file_name)
    else:
        true_train_label.append(file_name)

print(len(true_train_label))
print(len(true_test_label))
print(true_train_label)
print(true_test_label)

test_label = ['pancreas_021.nii.gz', 'pancreas_024.nii.gz', 'pancreas_040.nii.gz', 'pancreas_041.nii.gz',
              'pancreas_042.nii.gz', 'pancreas_045.nii.gz', 'pancreas_051.nii.gz', 'pancreas_058.nii.gz',
              'pancreas_067.nii.gz', 'pancreas_071.nii.gz', 'pancreas_075.nii.gz', 'pancreas_077.nii.gz',
              'pancreas_087.nii.gz', 'pancreas_089.nii.gz', 'pancreas_092.nii.gz', 'pancreas_095.nii.gz',
              'pancreas_110.nii.gz', 'pancreas_119.nii.gz', 'pancreas_138.nii.gz', 'pancreas_145.nii.gz',
              'pancreas_147.nii.gz', 'pancreas_166.nii.gz', 'pancreas_169.nii.gz', 'pancreas_170.nii.gz',
              'pancreas_175.nii.gz', 'pancreas_180.nii.gz', 'pancreas_186.nii.gz', 'pancreas_191.nii.gz',
              'pancreas_193.nii.gz', 'pancreas_194.nii.gz', 'pancreas_213.nii.gz', 'pancreas_222.nii.gz',
              'pancreas_225.nii.gz', 'pancreas_226.nii.gz', 'pancreas_235.nii.gz', 'pancreas_256.nii.gz',
              'pancreas_261.nii.gz', 'pancreas_284.nii.gz', 'pancreas_286.nii.gz', 'pancreas_290.nii.gz',
              'pancreas_294.nii.gz', 'pancreas_299.nii.gz', 'pancreas_305.nii.gz', 'pancreas_312.nii.gz',
              'pancreas_315.nii.gz', 'pancreas_320.nii.gz', 'pancreas_336.nii.gz', 'pancreas_343.nii.gz',
              'pancreas_364.nii.gz', 'pancreas_367.nii.gz', 'pancreas_370.nii.gz', 'pancreas_372.nii.gz',
              'pancreas_385.nii.gz', 'pancreas_386.nii.gz', 'pancreas_398.nii.gz', 'pancreas_401.nii.gz',
              'pancreas_411.nii.gz', 'pancreas_415.nii.gz', 'pancreas_422.nii.gz', 'pancreas_423.nii.gz',
              'pancreas_425.nii.gz', 'pancreas_436.nii.gz', 'pancreas_441.nii.gz', 'pancreas_442.nii.gz',
              'pancreas_444.nii.gz', 'pancreas_446.nii.gz', 'pancreas_466.nii.gz', 'pancreas_476.nii.gz',
              'pancreas_485.nii.gz', 'pancreas_487.nii.gz', 'pancreas_490.nii.gz', 'pancreas_494.nii.gz',
              'pancreas_502.nii.gz']
train_label = ['pancreas_001.nii.gz', 'pancreas_004.nii.gz', 'pancreas_005.nii.gz', 'pancreas_006.nii.gz',
               'pancreas_010.nii.gz', 'pancreas_012.nii.gz', 'pancreas_015.nii.gz', 'pancreas_016.nii.gz',
               'pancreas_018.nii.gz', 'pancreas_019.nii.gz', 'pancreas_025.nii.gz', 'pancreas_028.nii.gz',
               'pancreas_029.nii.gz', 'pancreas_032.nii.gz', 'pancreas_035.nii.gz', 'pancreas_037.nii.gz',
               'pancreas_043.nii.gz', 'pancreas_046.nii.gz', 'pancreas_048.nii.gz', 'pancreas_049.nii.gz',
               'pancreas_050.nii.gz', 'pancreas_052.nii.gz', 'pancreas_055.nii.gz', 'pancreas_056.nii.gz',
               'pancreas_061.nii.gz', 'pancreas_064.nii.gz', 'pancreas_066.nii.gz', 'pancreas_069.nii.gz',
               'pancreas_070.nii.gz', 'pancreas_074.nii.gz', 'pancreas_078.nii.gz', 'pancreas_080.nii.gz',
               'pancreas_081.nii.gz', 'pancreas_083.nii.gz', 'pancreas_084.nii.gz', 'pancreas_086.nii.gz',
               'pancreas_088.nii.gz', 'pancreas_091.nii.gz', 'pancreas_093.nii.gz', 'pancreas_094.nii.gz',
               'pancreas_096.nii.gz', 'pancreas_098.nii.gz', 'pancreas_099.nii.gz', 'pancreas_100.nii.gz',
               'pancreas_101.nii.gz', 'pancreas_102.nii.gz', 'pancreas_103.nii.gz', 'pancreas_104.nii.gz',
               'pancreas_105.nii.gz', 'pancreas_106.nii.gz', 'pancreas_107.nii.gz', 'pancreas_109.nii.gz',
               'pancreas_111.nii.gz', 'pancreas_113.nii.gz', 'pancreas_114.nii.gz', 'pancreas_117.nii.gz',
               'pancreas_120.nii.gz', 'pancreas_122.nii.gz', 'pancreas_124.nii.gz', 'pancreas_125.nii.gz',
               'pancreas_126.nii.gz', 'pancreas_127.nii.gz', 'pancreas_129.nii.gz', 'pancreas_130.nii.gz',
               'pancreas_131.nii.gz', 'pancreas_135.nii.gz', 'pancreas_137.nii.gz', 'pancreas_140.nii.gz',
               'pancreas_148.nii.gz', 'pancreas_149.nii.gz', 'pancreas_155.nii.gz', 'pancreas_157.nii.gz',
               'pancreas_158.nii.gz', 'pancreas_159.nii.gz', 'pancreas_160.nii.gz', 'pancreas_165.nii.gz',
               'pancreas_167.nii.gz', 'pancreas_172.nii.gz', 'pancreas_173.nii.gz', 'pancreas_178.nii.gz',
               'pancreas_179.nii.gz', 'pancreas_181.nii.gz', 'pancreas_182.nii.gz', 'pancreas_183.nii.gz',
               'pancreas_187.nii.gz', 'pancreas_196.nii.gz', 'pancreas_197.nii.gz', 'pancreas_198.nii.gz',
               'pancreas_199.nii.gz', 'pancreas_200.nii.gz', 'pancreas_201.nii.gz', 'pancreas_203.nii.gz',
               'pancreas_204.nii.gz', 'pancreas_207.nii.gz', 'pancreas_209.nii.gz', 'pancreas_210.nii.gz',
               'pancreas_211.nii.gz', 'pancreas_212.nii.gz', 'pancreas_214.nii.gz', 'pancreas_215.nii.gz',
               'pancreas_217.nii.gz', 'pancreas_218.nii.gz', 'pancreas_219.nii.gz', 'pancreas_224.nii.gz',
               'pancreas_227.nii.gz', 'pancreas_228.nii.gz', 'pancreas_229.nii.gz', 'pancreas_230.nii.gz',
               'pancreas_231.nii.gz', 'pancreas_234.nii.gz', 'pancreas_236.nii.gz', 'pancreas_239.nii.gz',
               'pancreas_241.nii.gz', 'pancreas_242.nii.gz', 'pancreas_243.nii.gz', 'pancreas_244.nii.gz',
               'pancreas_246.nii.gz', 'pancreas_247.nii.gz', 'pancreas_249.nii.gz', 'pancreas_253.nii.gz',
               'pancreas_254.nii.gz', 'pancreas_255.nii.gz', 'pancreas_258.nii.gz', 'pancreas_259.nii.gz',
               'pancreas_262.nii.gz', 'pancreas_264.nii.gz', 'pancreas_265.nii.gz', 'pancreas_266.nii.gz',
               'pancreas_267.nii.gz', 'pancreas_268.nii.gz', 'pancreas_269.nii.gz', 'pancreas_270.nii.gz',
               'pancreas_274.nii.gz', 'pancreas_275.nii.gz', 'pancreas_276.nii.gz', 'pancreas_277.nii.gz',
               'pancreas_278.nii.gz', 'pancreas_279.nii.gz', 'pancreas_280.nii.gz', 'pancreas_283.nii.gz',
               'pancreas_285.nii.gz', 'pancreas_287.nii.gz', 'pancreas_289.nii.gz', 'pancreas_291.nii.gz',
               'pancreas_292.nii.gz', 'pancreas_293.nii.gz', 'pancreas_295.nii.gz', 'pancreas_296.nii.gz',
               'pancreas_297.nii.gz', 'pancreas_298.nii.gz', 'pancreas_300.nii.gz', 'pancreas_301.nii.gz',
               'pancreas_302.nii.gz', 'pancreas_303.nii.gz', 'pancreas_304.nii.gz', 'pancreas_308.nii.gz',
               'pancreas_309.nii.gz', 'pancreas_310.nii.gz', 'pancreas_311.nii.gz', 'pancreas_313.nii.gz',
               'pancreas_316.nii.gz', 'pancreas_318.nii.gz', 'pancreas_321.nii.gz', 'pancreas_323.nii.gz',
               'pancreas_325.nii.gz', 'pancreas_326.nii.gz', 'pancreas_327.nii.gz', 'pancreas_328.nii.gz',
               'pancreas_329.nii.gz', 'pancreas_330.nii.gz', 'pancreas_331.nii.gz', 'pancreas_333.nii.gz',
               'pancreas_334.nii.gz', 'pancreas_339.nii.gz', 'pancreas_342.nii.gz', 'pancreas_344.nii.gz',
               'pancreas_345.nii.gz', 'pancreas_346.nii.gz', 'pancreas_347.nii.gz', 'pancreas_348.nii.gz',
               'pancreas_350.nii.gz', 'pancreas_351.nii.gz', 'pancreas_354.nii.gz', 'pancreas_355.nii.gz',
               'pancreas_356.nii.gz', 'pancreas_357.nii.gz', 'pancreas_358.nii.gz', 'pancreas_360.nii.gz',
               'pancreas_361.nii.gz', 'pancreas_362.nii.gz', 'pancreas_365.nii.gz', 'pancreas_366.nii.gz',
               'pancreas_369.nii.gz', 'pancreas_374.nii.gz', 'pancreas_375.nii.gz', 'pancreas_376.nii.gz',
               'pancreas_377.nii.gz', 'pancreas_378.nii.gz', 'pancreas_379.nii.gz', 'pancreas_380.nii.gz',
               'pancreas_382.nii.gz', 'pancreas_387.nii.gz', 'pancreas_388.nii.gz', 'pancreas_389.nii.gz',
               'pancreas_391.nii.gz', 'pancreas_392.nii.gz', 'pancreas_393.nii.gz', 'pancreas_395.nii.gz',
               'pancreas_399.nii.gz', 'pancreas_400.nii.gz', 'pancreas_402.nii.gz', 'pancreas_404.nii.gz',
               'pancreas_405.nii.gz', 'pancreas_406.nii.gz', 'pancreas_409.nii.gz', 'pancreas_410.nii.gz',
               'pancreas_412.nii.gz', 'pancreas_413.nii.gz', 'pancreas_414.nii.gz', 'pancreas_416.nii.gz',
               'pancreas_418.nii.gz', 'pancreas_419.nii.gz', 'pancreas_421.nii.gz', 'pancreas_424.nii.gz',
               'pancreas_426.nii.gz', 'pancreas_427.nii.gz', 'pancreas_428.nii.gz', 'pancreas_429.nii.gz',
               'pancreas_430.nii.gz', 'pancreas_431.nii.gz', 'pancreas_432.nii.gz', 'pancreas_433.nii.gz',
               'pancreas_434.nii.gz', 'pancreas_435.nii.gz', 'pancreas_437.nii.gz', 'pancreas_438.nii.gz',
               'pancreas_439.nii.gz', 'pancreas_440.nii.gz', 'pancreas_443.nii.gz', 'pancreas_445.nii.gz',
               'pancreas_447.nii.gz', 'pancreas_448.nii.gz', 'pancreas_449.nii.gz', 'pancreas_450.nii.gz',
               'pancreas_451.nii.gz', 'pancreas_452.nii.gz', 'pancreas_453.nii.gz', 'pancreas_454.nii.gz',
               'pancreas_455.nii.gz', 'pancreas_456.nii.gz', 'pancreas_457.nii.gz', 'pancreas_458.nii.gz',
               'pancreas_459.nii.gz', 'pancreas_460.nii.gz', 'pancreas_461.nii.gz', 'pancreas_462.nii.gz',
               'pancreas_463.nii.gz', 'pancreas_464.nii.gz', 'pancreas_465.nii.gz', 'pancreas_467.nii.gz',
               'pancreas_468.nii.gz', 'pancreas_469.nii.gz', 'pancreas_470.nii.gz', 'pancreas_471.nii.gz',
               'pancreas_472.nii.gz', 'pancreas_473.nii.gz', 'pancreas_474.nii.gz', 'pancreas_475.nii.gz',
               'pancreas_477.nii.gz', 'pancreas_478.nii.gz', 'pancreas_479.nii.gz', 'pancreas_480.nii.gz',
               'pancreas_481.nii.gz', 'pancreas_482.nii.gz', 'pancreas_483.nii.gz', 'pancreas_484.nii.gz',
               'pancreas_486.nii.gz', 'pancreas_488.nii.gz', 'pancreas_489.nii.gz', 'pancreas_491.nii.gz',
               'pancreas_492.nii.gz', 'pancreas_493.nii.gz', 'pancreas_495.nii.gz', 'pancreas_496.nii.gz',
               'pancreas_497.nii.gz', 'pancreas_498.nii.gz', 'pancreas_499.nii.gz', 'pancreas_500.nii.gz',
               'pancreas_501.nii.gz', 'pancreas_503.nii.gz']
