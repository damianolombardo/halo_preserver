import halo_preserver_prod
gamertags = ["MSgates123", "McVinny"]
for gamertag in gamertags:
	halo_preserver_prod.halo2_get_files(gamertag)
	halo_preserver_prod.halo3_get_files(gamertag)
	halo_preserver_prod.halo3_get_campaign_files(gamertag)
	halo_preserver_prod.halo3_main_stats_page(gamertag)
	boolean_options = [True,False]
	for individual_weapons in boolean_options:
		for kills in boolean_options:
			halo_preserver_prod.halo3_get_heatmap_images(gamertag,individual_weapons=individual_weapons,kills=kills)

