from Model import *

if __name__ == '__main__':
    dataset_seq = [1, 2, 3, 4]
    cm_seq = [1, 2]
    prod_seq = [1, 2]
    wd_seq = [1, 2, 3]

    for data_setting in dataset_seq:
        dataset_name = 'email' * (data_setting == 1) + 'dnc_email' * (data_setting == 2) + \
                       'email_Eu_core' * (data_setting == 3) + 'NetHEPT' * (data_setting == 4)
        for cm in cm_seq:
            cascade_model = 'ic' * (cm == 1) + 'wc' * (cm == 2)
            for prod_setting in prod_seq:
                product_name = 'item_lphc' * (prod_setting == 1) + 'item_hplc' * (prod_setting == 2)

                Model('mdag1', dataset_name, product_name, cascade_model).model_dag(1, r_flag=False)
                Model('mdag1r', dataset_name, product_name, cascade_model).model_dag(1, r_flag=True)
                Model('mdag2', dataset_name, product_name, cascade_model).model_dag(2, r_flag=False)
                Model('mdag2r', dataset_name, product_name, cascade_model).model_dag(2, r_flag=True)

                for wd in wd_seq:
                    wallet_distribution_type = 'm50e25' * (wd == 1) + 'm66e34' * (wd == 2) + 'm99e96' * (wd == 3)

                    Model('mdag1epw', dataset_name, product_name, cascade_model, wallet_distribution_type).model_dag(1, r_flag=False)
                    Model('mdag1repw', dataset_name, product_name, cascade_model, wallet_distribution_type).model_dag(1, r_flag=True)
                    Model('mdag2epw', dataset_name, product_name, cascade_model, wallet_distribution_type).model_dag(2, r_flag=False)
                    Model('mdag2repw', dataset_name, product_name, cascade_model, wallet_distribution_type).model_dag(2, r_flag=True)

                for times in range(10):
                    Model('mng_' + str(times), dataset_name, product_name, cascade_model).model_ng(r_flag=False)
                    Model('mngr_' + str(times), dataset_name, product_name, cascade_model).model_ng(r_flag=True)
                    Model('mhd_' + str(times), dataset_name, product_name, cascade_model).model_hd()
                    Model('mr_' + str(times), dataset_name, product_name, cascade_model).model_r()
                    Model('mpmis_' + str(times), dataset_name, product_name, cascade_model).model_pmis()
                    Model('mbcs_' + str(times), dataset_name, product_name, cascade_model).model_bcs()

                    for wd in wd_seq:
                        wallet_distribution_type = 'm50e25' * (wd == 1) + 'm99e96' * (wd == 2) + 'm66e34' * (wd == 3)
                        Model('mngepw_' + str(times), dataset_name, product_name, cascade_model, wallet_distribution_type).model_ng(r_flag=False)
                        Model('mngrepw_' + str(times), dataset_name, product_name, cascade_model, wallet_distribution_type).model_ng(r_flag=True)
                        Model('mpmisepw_' + str(times), dataset_name, product_name, cascade_model, wallet_distribution_type).model_pmis()
                        Model('mbcsepw_' + str(times), dataset_name, product_name, cascade_model, wallet_distribution_type).model_bcs()