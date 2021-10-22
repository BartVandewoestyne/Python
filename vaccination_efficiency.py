# Bron: https://statbel.fgov.be/nl/themas/bevolking/structuur-van-de-bevolking
aantal_inwoners_vlaanderen = 6653062
aantal_inwoners_brussel    = 1219970
aantal_inwoners_wallonie   = 3648206

gevaxt_vlaanderen = (0 + 0.9 + 8.8)*aantal_inwoners_vlaanderen/100000
niet_gevaxt_vlaanderen = (1.6 + 9.8 + 25.3)*aantal_inwoners_vlaanderen/100000

gevaxt_brussel = (0 + 1.6 + 18.6)*aantal_inwoners_brussel/100000
niet_gevaxt_brussel = (3.3 + 9.7 + 50.4)*aantal_inwoners_brussel/100000

gevaxt_wallonie = (1.2 + 1.5 + 11.5)*aantal_inwoners_wallonie/100000
niet_gevaxt_wallonie = (1.2 + 5.2 + 40.5)*aantal_inwoners_wallonie/100000

total_gevaxt = gevaxt_vlaanderen + gevaxt_brussel + gevaxt_wallonie
total_niet_gevaxt = niet_gevaxt_vlaanderen + niet_gevaxt_brussel + niet_gevaxt_wallonie
total = total_gevaxt + total_niet_gevaxt

percentage_gevaxt = total_gevaxt / total
percentage_niet_gevaxt = total_niet_gevaxt / total

print("percentage gevaxt = ", percentage_gevaxt)
print("percentage niet gevaxt = ", percentage_niet_gevaxt)
