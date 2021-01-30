import halo_preserver_prod
gamertags = ["MSgates123", "McVinny"]
for gamertag in gamertags:
	try:
	halo_preserver_prod.halo2_get_files(gamertag)
	except:
		print(f'halo2_get_files failed for {gamertag}')
	try:	
	halo_preserver_prod.halo3_get_files(gamertag)
	except:
		print(f'halo3_get_files failed for {gamertag}')
	try:	
	halo_preserver_prod.halo3_get_campaign_files(gamertag)
	except:
		print(f'halo3_get_campaign_files failed for {gamertag}')
	try:	
	halo_preserver_prod.halo3_main_stats_page(gamertag)
	except:
		print(f'halo3_main_stats_page failed for {gamertag}')
	boolean_options = [True,False]
	for individual_weapons in boolean_options:
		for kills in boolean_options:
			try:	
			halo_preserver_prod.halo3_get_heatmap_images(gamertag,individual_weapons=individual_weapons,kills=kills)
			except:
				print(f'halo3_get_heatmap_images failed for {gamertag}, individual_weapons={individual_weapons},kills={kills}')


