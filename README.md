#Here is the GDR_calc_result
#It's name in the main brach of repository is 'AberaTest__abera_distmat_list__population__gdr.tsv'

---------------------------------------------------------------------------------------------------------------------------------------------------------
# here I had added a "Bootstrapping results", "yaml file for bootstrapp", "yaml file for estimation of P Values" and their names in the main branch of repository are as the following:
#Bootstrap_result.tsv
#willowj_bootstrap_v2.yaml
#willowj_estimatePValues_v2.yaml

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#And when I tried to run the command line for the estimation of P_Values I was get the following error:
#My yaml file is: "willowj_estimatePValues_v2.yaml"

#The command I was used to run: 
#java -jar -Dlog4j.configurationFile=file:"/home/abera/data1/data1/willowTestData/gdr.log4j2.xml" WillowJ.jar -c "/home/abera/data1/data1/willowTestData/willowj_estimatePValues_v2.yaml" 

#The error I found: 
#20:31:27.688 [main] ERROR willow.GDRCalculator - ------error reading CDR/GDR result file </home/abera/data1/data1/willowTestData/#GDRcalculationResultsJ/AberaTest_estimatePValues__abera_distmat_list__population__gdr.tsv>
#20:31:27.689 [main] ERROR willow.GDRCalculator - /home/abera/data1/data1/willowTestData/GDRcalculationResultsJ/AberaTest_estimatePValues__abera_distmat_list__population__gdr.tsv
#java.io.IOException: java.nio.file.NoSuchFileException: /home/abera/data1/data1/willowTestData/GDRcalculationResultsJ/AberaTest_estimatePValues__abera_distmat_list__population__gdr.tsv
#After the above error was fixed both new bootstrap and P_Values are added on GitHub repository:
#AberaTest_bootstrap__abera_distmat_list__population__gdr.tsv
#AberaTest__abera_distmat_list__population__pvals.tsv
#Then after here is a following Adjusted P_Values:
#top_features_with_lowest_pvals.csv





