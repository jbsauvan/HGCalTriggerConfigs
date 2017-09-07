from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'NuGun_PU200_L1TDR'
config.General.workArea = 'jobs'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'produce_clusteronly_geomV7_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.inputDataset = '/SingleNeutrino/PhaseIISpring17D-PU200_90X_upgrade2023_realistic_v9-v1/GEN-SIM-DIGI-RAW'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 15
config.Data.outLFNDirBase = '/store/user/jsauvan/HGCAL/'
config.Data.publication = False
config.Data.outputDatasetTag = 'NuGun_PU200_L1TDR_ClustersOnly'

config.section_("Site")
config.Site.storageSite = 'T2_FR_GRIF_LLR'
