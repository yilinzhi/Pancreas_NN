# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2021/08/20 11:39
# @Author  : Yi
# @FileName: data_json.py

"""
    TODO：
        自定义dataset.json
"""

from collections import OrderedDict
from batchgenerators.utilities.file_and_folder_operations import save_json

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


def main():
    """生成dataset.json文件，符合nnUNet的要求。

    :return:
    """
    foldername = "Task503_Pancreas"
    description = "Pancreas segmentation"
    numTraining = 290
    numTest = 73
    numClass = 2
    json_dict = OrderedDict()
    json_dict['name'] = foldername
    json_dict['description'] = description
    json_dict['tensorImageSize'] = "4D"
    json_dict['reference'] = "TBA"
    json_dict['licence'] = "CC-BY"
    json_dict['release'] = "0.0"
    json_dict['modality'] = {
        "0": "CT",
    }

    # labels的数值为0,1,...,连续的数值
    json_dict['labels'] = {"0": "background", "1": "labels"}

    json_dict['numTraining'] = numTraining
    json_dict['numTest'] = numTest

    json_dict['training'] = [{
        'image': "./imagesTr/{}".format(
            i),
        "label": "./labelsTr/{}".format(
            i)}
        for i in train_label]

    json_dict['test'] = [
        "./imagesTs/{}".format(
            i)
        for i in test_label]

    save_json(json_dict,
              "/data/yilinzhi/Segmentation/nnUNetFrame/DataSets/nnUNet_raw/nnUNet_raw_data/Task503_Pancreas/dataset.json")


if __name__ == "__main__":
    main()
