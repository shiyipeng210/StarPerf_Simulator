'''

Author : yunanhou

Date : 2023/11/11

Function : Coverage rate test cases at two locations under Constellation +Gird working mode

'''

import src.constellation_generation.by_XML.constellation_configuration as constellation_configuration
import src.XML_constellation.constellation_connectivity.connectivity_mode_plugin_manager as connectivity_mode_plugin_manager
import src.XML_constellation.constellation_evaluation.exists_ISL.coverage as COVERAGE

# Coverage rate test cases at two locations under Constellation +Gird working mode
def coverage():
    dT=1000
    constellation_name = "Starlink"
    # generate the constellations
    constellation= constellation_configuration.constellation_configuration(dT, constellation_name=constellation_name)
    # initialize the connectivity mode plugin manager
    connectionModePluginManager = connectivity_mode_plugin_manager.connectivity_mode_plugin_manager()
    # execute the connectivity mode and build ISLs between satellites
    connectionModePluginManager.execute_connection_policy(constellation=constellation , dT=dT)
    coverage= COVERAGE.coverage(constellation.constellation_name, dT, constellation.shells[0])
    print("\t\t\tThe coverage rates of the constellation for every timeslot are : " , coverage)
    satellite_in_latitude , satellite_in_longitude = COVERAGE.coverage_aggregated_by_latitude_and_longitude(constellation.constellation_name,
                                                                                                            dT, constellation.shells[0])
    print("\t\t\tThe average number of visible satellites per timeslot is distributed by latitude : " , satellite_in_latitude)
    print("\t\t\tThe average number of visible satellites per timeslot is distributed by longitude : " , satellite_in_longitude)

    output_file = "coverage_output.txt"
    # 打开文件进行写操作
    with open(output_file, "a") as f:  # 使用 "a" 模式，以便追加内容，而不是覆盖
        # 保存 coverage 数据
        f.write(f"\t\t\tThe coverage rates of the constellation for every timeslot are : {coverage}\n")
        # 获取卫星经纬度分布
        satellite_in_latitude, satellite_in_longitude = COVERAGE.coverage_aggregated_by_latitude_and_longitude(
            constellation.constellation_name, dT, constellation.shells[0]
        )
        # 保存卫星分布的纬度信息
        f.write(
            f"\t\t\tThe average number of visible satellites per timeslot is distributed by latitude : {satellite_in_latitude}\n")
        # 保存卫星分布的经度信息
        f.write(
            f"\t\t\tThe average number of visible satellites per timeslot is distributed by longitude : {satellite_in_longitude}\n")

if __name__ == "__main__":
    coverage()