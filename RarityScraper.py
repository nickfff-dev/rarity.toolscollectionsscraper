import re
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import Select
import time
import re


driver = webdriver.Chrome()
page ="https://rarity.tools/osiris-cosmic-kids"

def msema(page):
    traitz = {"traitname":[],"traitdata-value":[],"valuetotal":[]}

    profilez = {"Name":[], "Link": [], "Total Mints":[], "Min Trait Count":[],"Max Trait Count":[], "Number of Different Traits":[],"traitcount":[],"total":[]}

    profilez["Name"].append(page.rsplit('/', 1)[-1])
    profilez["Link"].append(page)


    driver.get(page)

    time.sleep(15)

    driver.find_element_by_css_selector("#__layout > div > div.flex-1.overflow-hidden.lg\:flex.lg\:flex-row.bg > div.max-h-full.pt-3.borderLine.bg.dark\:text-gray-200.sidebar.lg\:overflow-y-scroll.scrollColor > div.mb-6.lg\:block.hidden > div > input.inline-block.px-2.my-2.text-sm.text-white.bg-transparent.bg-pink-700.border.border-transparent.rounded-lg.outline-none.cursor-pointer.dark\:hover\:bg-pink-900.dark\:bg-pink-800.hover\:bg-pink-800.ml-2text-base.btn.search").click()
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    kwama = soup.find_all("div", class_="mb-2")

    for vitu in kwama:
        all_values = vitu.find_all("div", attrs={"class": "flex-grow overflow-hidden"})
        for div in all_values:
            try:
                traitz["traitdata-value"].append(str(div.text.replace('\n', ' ').strip()))
            except:
                traitz["traitdata-value"].append("null")

            try:
                traitz["traitname"].append(vitu.find("span", attrs={"class": "font-bold textColor700"}).text)
            except:
                traitz["traitname"].append("null")
        trait_totals= vitu.find_all("div", attrs={"class": "w-12 pr-1 m-px ml-1.5 text-right bg-white dark:bg-gray-200 rounded font-medium text-gray-400 dark:text-gray-600"})
        for span in trait_totals:
            try:
                traitz["valuetotal"].append(int(span.text.replace('\n', ' ').strip()))
            except:
                traitz["valuetotal"].append("null")



    profilez["Total Mints"].append(driver.find_element_by_css_selector("#__layout > div > div.flex-1.overflow-hidden.lg\:flex.lg\:flex-row.bg > div.bg.max-h-full.px-0\.5.lg\:px-2.text-lg.textColor600.bg-white.lg\:overflow-y-scroll.lg\:flex-grow.scrollColor > div.sticky.top-0.z-10.flex.flex-col.items-center.pb-2.pt-1\.5.pr-12.bg.pl-9 > div:nth-child(2) > div.flex.flex-row.items-center.mr-2.text-sm.font-bold > div:nth-child(1)").text)

    try:                                            
        total  = driver.find_elements_by_css_selector("#__layout > div > div.flex-1.overflow-hidden.lg\:flex.lg\:flex-row.bg > div.max-h-full.pt-3.borderLine.bg.dark\:text-gray-200.sidebar.lg\:overflow-y-scroll.scrollColor > div.mb-6.lg\:block.hidden > div:nth-child(13) > div > div > div > div > div.w-12.pr-1.m-px.ml-1\.5.text-right.bg-white.dark\:bg-gray-200.rounded.font-medium.text-gray-400.dark\:text-gray-600")
        for tz in total:
            profilez["total"].append(int(tz.text))
    except:
        profilez["total"] = 0

    try:
        traitcount = driver.find_elements_by_css_selector("#__layout > div > div.flex-1.overflow-hidden.lg\:flex.lg\:flex-row.bg > div.max-h-full.pt-3.borderLine.bg.dark\:text-gray-200.sidebar.lg\:overflow-y-scroll.scrollColor > div.mb-6.lg\:block.hidden > div:nth-child(13) > div > div > div > div > div.flex-grow.overflow-hidden")
        for tc in traitcount:
            profilez["traitcount"].append(int(tc.text))
    except:
        profilez["traitcount"] = 0
        profilez["total"].clear()

    try:
        trr =  profilez["total"].index(min(profilez["total"]))
        profilez["Min Trait Count"]= profilez["traitcount"][trr]

    except:

        profilez["Min Trait Count"] = 0

    try:
        trr2 = profilez["total"].index(max(profilez["total"]))
        profilez["Max Trait Count"]= profilez["traitcount"][trr2]

    except:

        profilez["Max Trait Count"] = 0
    profilez["Number of Different Traits"] =len(traitz["traitname"])-len(profilez["traitcount"])




    df = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in traitz.items()]))
    frr = df.loc[df["traitname"] != "Trait Count" ]
    df2 = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in profilez.items()]))


    # new_df  = frr.groupby(["traitname"]).sum().reset_index()

    new_df = frr.groupby(["traitname"])
    new_df = new_df[["valuetotal"]].sum().add_prefix("Sum_of_").reset_index()

    fname = str(profilez["Name"][0]).replace("][/'=&:;", "")+".csv"

    df3 = pd.concat([frr, new_df,df2], axis=1)
    print(df3)

    return df3.to_csv(fname)


iko = []

urls =['https://rarity.tools/cryptoadz-by-gremplin','https://rarity.tools/cryptopunks','https://rarity.tools/thehumanoids','https://rarity.tools/boredapeyachtclub','https://rarity.tools/bears-deluxe','https://rarity.tools/cyberkongz','https://rarity.tools/cool-cats-nft','https://rarity.tools/galacticapes','https://rarity.tools/the-doge-pound','https://rarity.tools/mutant-ape-yacht-club','https://rarity.tools/official-surreals','https://rarity.tools/peaceful-groupies','https://rarity.tools/cryptodickbutts-s3','https://rarity.tools/winterbears','https://rarity.tools/theyakuzacatssociety','https://rarity.tools/cyberkongz-vx','https://rarity.tools/hashmasks','https://rarity.tools/capsulehouse','https://rarity.tools/fly-frogs','https://rarity.tools/sneaky-vampire-syndicate','https://rarity.tools/lazy-lions','https://rarity.tools/pudgypenguins','https://rarity.tools/lootproject','https://rarity.tools/meebits','https://rarity.tools/supducks','https://rarity.tools/fluf-world','https://rarity.tools/dirtybird-flight-club','https://rarity.tools/chill-frogs','https://rarity.tools/fastfoodfrenscollection','https://rarity.tools/loopy-donuts','https://rarity.tools/galaxy-fight-club','https://rarity.tools/ape-gang','https://rarity.tools/dystopunks-v2','https://rarity.tools/gutterdogs','https://rarity.tools/robotos-official','https://rarity.tools/collectvox','https://rarity.tools/world-of-women-nft','https://rarity.tools/deadfellaz','https://rarity.tools/sipheriansurge','https://rarity.tools/thecryptodads','https://rarity.tools/doge-pound-puppies-real','https://rarity.tools/niftydegen','https://rarity.tools/wannapandaofficial','https://rarity.tools/tinypaws','https://rarity.tools/acclimatedmooncats','https://rarity.tools/veefriends','https://rarity.tools/onchainmonkey','https://rarity.tools/bored-ape-kennel-club','https://rarity.tools/divine-zodiac','https://rarity.tools/ununicornsofficial','https://rarity.tools/foxyfamnft','https://rarity.tools/kingfrogs','https://rarity.tools/bastard-penguins','https://rarity.tools/0n1-force','https://rarity.tools/spaceboysnft','https://rarity.tools/bubblegumkids','https://rarity.tools/sappy-seals','https://rarity.tools/gutterpigeons','https://rarity.tools/wicked-ape-bone-club','https://rarity.tools/byopills','https://rarity.tools/paladin-pandas','https://rarity.tools/the-wanderers','https://rarity.tools/rumble-kong-league','https://rarity.tools/wearetheoutkast','https://rarity.tools/obitsofficial','https://rarity.tools/gorillanemesis','https://rarity.tools/fanggangnft','https://rarity.tools/the-crypto-chicks','https://rarity.tools/adam-bomb-squad','https://rarity.tools/bad-bunnies-nft','https://rarity.tools/bossbeauties','https://rarity.tools/pugfrens','https://rarity.tools/theclaylings','https://rarity.tools/wicked-hound-bone-club','https://rarity.tools/guttercatgang','https://rarity.tools/marscatsvoyage','https://rarity.tools/woodies-generative','https://rarity.tools/magic-mushroom-clubhouse','https://rarity.tools/superyeti','https://rarity.tools/roaringleaders','https://rarity.tools/24px','https://rarity.tools/qubits-on-the-ice','https://rarity.tools/the-sevens-official','https://rarity.tools/dapperdinosnft','https://rarity.tools/space-punks-club','https://rarity.tools/bonsai-zenft','https://rarity.tools/grillzgang','https://rarity.tools/dreamloops','https://rarity.tools/g-evols','https://rarity.tools/animetas','https://rarity.tools/sadgirlsbar','https://rarity.tools/forgottenruneswizardscult','https://rarity.tools/fvck-crystal','https://rarity.tools/flowtys','https://rarity.tools/mightybabydragons','https://rarity.tools/nftsiblings','https://rarity.tools/monster-blocks','https://rarity.tools/satoshibles','https://rarity.tools/koala-intelligence-agency','https://rarity.tools/bored-mummy-waking-up','https://rarity.tools/theplutoalliance','https://rarity.tools/gamblingapesofficial','https://rarity.tools/incognito-nft','https://rarity.tools/axolittles','https://rarity.tools/ethergals-community','https://rarity.tools/thewickedcraniums','https://rarity.tools/notorious-frogs','https://rarity.tools/0xvampire-project','https://rarity.tools/theninjahideout','https://rarity.tools/crypto-hobos','https://rarity.tools/crypto-duckies','https://rarity.tools/gutterrats','https://rarity.tools/omnimorphs','https://rarity.tools/bullsontheblock','https://rarity.tools/skvllpvnkz-hideout','https://rarity.tools/superfuzz-the-good-guys','https://rarity.tools/nfh','https://rarity.tools/uwucrew','https://rarity.tools/purrnelopes-country-club','https://rarity.tools/badassbulls','https://rarity.tools/gauntlets','https://rarity.tools/mutantkongz','https://rarity.tools/voxies','https://rarity.tools/bullseum','https://rarity.tools/the-moon-boyz','https://rarity.tools/dogs-unchained','https://rarity.tools/stoner-cats-official','https://rarity.tools/london-gift-v2','https://rarity.tools/savage-droids','https://rarity.tools/cartlads','https://rarity.tools/encryptas-1','https://rarity.tools/thepppandas','https://rarity.tools/fast-food-punks','https://rarity.tools/kgds','https://rarity.tools/sympathyforthedevils','https://rarity.tools/cryptocannabisclub','https://rarity.tools/deadheads','https://rarity.tools/maisondegoat','https://rarity.tools/lonelyalienspaceclub','https://rarity.tools/facanft','https://rarity.tools/goonsofbalatroon','https://rarity.tools/vogu','https://rarity.tools/avastar','https://rarity.tools/avariksagauniverse','https://rarity.tools/lysergiclabsshroomz','https://rarity.tools/crypto-hodlers-nft','https://rarity.tools/primate-social-society-official','https://rarity.tools/penguin-fight-club','https://rarity.tools/thedudes','https://rarity.tools/lambduhs','https://rarity.tools/thekillaz','https://rarity.tools/sidus-nft-heroes','https://rarity.tools/crypto-pills-by-micha-klein','https://rarity.tools/visitors-of-imma-degen','https://rarity.tools/guardians-of-the-metaverse','https://rarity.tools/buzzedbears','https://rarity.tools/topdogbeachclub','https://rarity.tools/bearmarketbears','https://rarity.tools/bastard-gan-punks-v2','https://rarity.tools/chibi-apes','https://rarity.tools/warriors-of-aradena','https://rarity.tools/dope-shibas','https://rarity.tools/richkidsofficial','https://rarity.tools/lady-killaz','https://rarity.tools/secretsocietyofwhales','https://rarity.tools/chiptos','https://rarity.tools/theprojecturs','https://rarity.tools/rebelbots','https://rarity.tools/roguesocietybot','https://rarity.tools/ready-player-cat-nft','https://rarity.tools/lumpsworld','https://rarity.tools/fatales','https://rarity.tools/based-fish-mafia','https://rarity.tools/bcsnft','https://rarity.tools/fusionape','https://rarity.tools/spacepoggers','https://rarity.tools/tie-dye-ninjas','https://rarity.tools/great-ape-society','https://rarity.tools/sushiverse-official','https://rarity.tools/hashguise-gen-1','https://rarity.tools/holycows','https://rarity.tools/space-dinos-club','https://rarity.tools/degengang','https://rarity.tools/thealienboy','https://rarity.tools/topcatbeachclub','https://rarity.tools/sad-frogs-district','https://rarity.tools/save-the-martians','https://rarity.tools/bored-mummy-baby-waking-up','https://rarity.tools/junkyarddogs','https://rarity.tools/bunkerbeasts','https://rarity.tools/frogsindisguise','https://rarity.tools/angryboarsnft','https://rarity.tools/clevergirlsnft','https://rarity.tools/deepseajelly','https://rarity.tools/fameladysquad','https://rarity.tools/thewynlambo','https://rarity.tools/chibidinos','https://rarity.tools/srsc','https://rarity.tools/epiceagles','https://rarity.tools/bullishllama','https://rarity.tools/dizzydragons','https://rarity.tools/royalsocietyofplayers','https://rarity.tools/blankfaceofficial','https://rarity.tools/royal-ceramic-club','https://rarity.tools/superfuzz-the-bad-batch','https://rarity.tools/cryptotrunks','https://rarity.tools/blox-blu','https://rarity.tools/bearsontheblock','https://rarity.tools/bad-kids-alley-official','https://rarity.tools/alphabetty-doodles','https://rarity.tools/apesofspace-official','https://rarity.tools/blobmob','https://rarity.tools/ethereans-official','https://rarity.tools/rivermen','https://rarity.tools/toolsofrock','https://rarity.tools/djenerates-clubbing-edition','https://rarity.tools/nobodyeth','https://rarity.tools/thestreetdawgs','https://rarity.tools/spaceshibas','https://rarity.tools/officialdogex','https://rarity.tools/weirdwhales','https://rarity.tools/genesis-blocks-art','https://rarity.tools/thelostglitches','https://rarity.tools/spunks-nft','https://rarity.tools/krazykoalas','https://rarity.tools/citizens-of-bulliever-island','https://rarity.tools/dropbearsnft','https://rarity.tools/lockdown-lemmings','https://rarity.tools/unusualwhalesnft','https://rarity.tools/super-bunnies','https://rarity.tools/darksuperbunnies','https://rarity.tools/misscryptoclub','https://rarity.tools/minimonkeymafia','https://rarity.tools/heroes-of-evermore','https://rarity.tools/beatniktikitribe','https://rarity.tools/cryptobabypunksopensea','https://rarity.tools/gluefactoryshow','https://rarity.tools/stripperville-nfts','https://rarity.tools/boring-bananas-company','https://rarity.tools/the-kittybutts','https://rarity.tools/the-unstable-horses-yard','https://rarity.tools/mighty-manateez','https://rarity.tools/leagueofsacreddevils','https://rarity.tools/chads-nft','https://rarity.tools/thewolfgang','https://rarity.tools/astro-frens','https://rarity.tools/ameegosofficialnft','https://rarity.tools/caninecartel','https://rarity.tools/pandadynasty','https://rarity.tools/theo-nft','https://rarity.tools/cybergirl-fashion','https://rarity.tools/party-penguins','https://rarity.tools/cunningfoxes','https://rarity.tools/happyland-gummy-bears-official','https://rarity.tools/slumdoge-billionaires','https://rarity.tools/mandelbrot-set-collection','https://rarity.tools/cryptoskulls','https://rarity.tools/afrodroids-by-owo','https://rarity.tools/blockchainbikers','https://rarity.tools/soccerdogeclub','https://rarity.tools/shaggy-sheep','https://rarity.tools/pudgy24pixelgang','https://rarity.tools/pork1984','https://rarity.tools/lostsoulssanctuary','https://rarity.tools/lostboy-nft','https://rarity.tools/farmers-marketverse-patrons','https://rarity.tools/ape-harbour-yachts','https://rarity.tools/bones-club-heritage','https://rarity.tools/deadbears-official','https://rarity.tools/the-birdhouse-official','https://rarity.tools/barn-owlz','https://rarity.tools/demonzv1','https://rarity.tools/lion-club','https://rarity.tools/punkcats','https://rarity.tools/pownft','https://rarity.tools/manekigang','https://rarity.tools/hall-of-fame-goat-lodge','https://rarity.tools/long-neckie-ladies','https://rarity.tools/crazy-lizard-army','https://rarity.tools/lucha-libre-knockout','https://rarity.tools/pixls-official','https://rarity.tools/niftyriots','https://rarity.tools/criminaldonkeys','https://rarity.tools/blazedcats','https://rarity.tools/luckymaneki','https://rarity.tools/chubbies','https://rarity.tools/monas','https://rarity.tools/wickedstallions','https://rarity.tools/dorkisofficial','https://rarity.tools/galactic-secret-agency','https://rarity.tools/svinsfarm','https://rarity.tools/covidpunksnft','https://rarity.tools/shabu-town-shibas','https://rarity.tools/pepperattack','https://rarity.tools/cryptosquatches','https://rarity.tools/untamed-elephants','https://rarity.tools/8bituniverse','https://rarity.tools/cryptofighters','https://rarity.tools/animathereum','https://rarity.tools/ciphersquares-official','https://rarity.tools/arabian-camels','https://rarity.tools/chainfaces','https://rarity.tools/royalsocietychips','https://rarity.tools/thekamagang','https://rarity.tools/spookies-nft','https://rarity.tools/osiris-cosmic-kids','https://rarity.tools/satoshifaces','https://rarity.tools/angels-of-aether','https://rarity.tools/moondogs-odyssey','https://rarity.tools/orcz-official','https://rarity.tools/obcofficial','https://rarity.tools/the-shark-cove','https://rarity.tools/crumbys-bakery','https://rarity.tools/raccoon-mafia','https://rarity.tools/cyphercity','https://rarity.tools/slacker-duck-pond','https://rarity.tools/hewerclan','https://rarity.tools/animalworldwar','https://rarity.tools/rebel-kids','https://rarity.tools/crypto-corgis','https://rarity.tools/neon-junkies','https://rarity.tools/crazy-dragon-corps','https://rarity.tools/mad-banana-union','https://rarity.tools/lobby-lobsters','https://rarity.tools/degenz','https://rarity.tools/nice-drips-','https://rarity.tools/sodabits','https://rarity.tools/monsterrehab','https://rarity.tools/creativeartquest','https://rarity.tools/slothz','https://rarity.tools/strawberrywtf','https://rarity.tools/shiba-society','https://rarity.tools/derpy-birbs','https://rarity.tools/myfuckingpickle','https://rarity.tools/nftlions','https://rarity.tools/hd--punks','https://rarity.tools/rickstro-frens','https://rarity.tools/bones-and-bananas','https://rarity.tools/hodlgangnft','https://rarity.tools/the-crypto-saints','https://rarity.tools/punkbabies','https://rarity.tools/kidpunks','https://rarity.tools/graycraft-2','https://rarity.tools/wildstagtreehouse','https://rarity.tools/shcv1','https://rarity.tools/waifusion','https://rarity.tools/bigbrainsociety','https://rarity.tools/stranger-eggz','https://rarity.tools/cryptofinney','https://rarity.tools/bit-wine','https://rarity.tools/baked-bears-beach-club','https://rarity.tools/ptbc','https://rarity.tools/wannabesmusicclub','https://rarity.tools/the-monstrocities','https://rarity.tools/keplerscivilsociety','https://rarity.tools/catshitcrazy','https://rarity.tools/mad-cat-militia','https://rarity.tools/re-genz','https://rarity.tools/floyds-world','https://rarity.tools/nftboy-bored-ape-racers','https://rarity.tools/polar-pals-bobsledding','https://rarity.tools/muttniks','https://rarity.tools/degens-farm','https://rarity.tools/raccoon-secret-society','https://rarity.tools/absurdarboretum','https://rarity.tools/lonelyplanetspaceobservatory','https://rarity.tools/thewonderquest','https://rarity.tools/zunks','https://rarity.tools/tokenmonnft','https://rarity.tools/highflyers','https://rarity.tools/long-neckie-fellas','https://rarity.tools/naughty-tigers-costume-club','https://rarity.tools/theshrunkenheadz','https://rarity.tools/baby-combat-bots-g1','https://rarity.tools/recklesswhales','https://rarity.tools/crazy-crows-chess-club','https://rarity.tools/mutant-ape-pixel-club-official','https://rarity.tools/ruumz','https://rarity.tools/the4001project','https://rarity.tools/thenanoz','https://rarity.tools/goblin-goons','https://rarity.tools/deebies','https://rarity.tools/misfit-university-official','https://rarity.tools/astrohedz','https://rarity.tools/hype-hippo-io','https://rarity.tools/altdoges','https://rarity.tools/unitedpunksunion','https://rarity.tools/pineapplesdayout','https://rarity.tools/proceduralspace','https://rarity.tools/ragingrhinos','https://rarity.tools/fuckintrolls','https://rarity.tools/cryptotuners','https://rarity.tools/chunky-cow-club-tour-official','https://rarity.tools/hatch-your-destiny','https://rarity.tools/starchain-official','https://rarity.tools/etheremura','https://rarity.tools/cutepigclub','https://rarity.tools/raccoonsclub','https://rarity.tools/kokeshi-world','https://rarity.tools/dogepirates','https://rarity.tools/hodlheads','https://rarity.tools/rabbit-college-club','https://rarity.tools/cryptoghostsnft','https://rarity.tools/pymons','https://rarity.tools/minimints','https://rarity.tools/noobsnft','https://rarity.tools/the-space-doge','https://rarity.tools/pandagolfsquad','https://rarity.tools/devious-demon-dudes','https://rarity.tools/scoopdogsquad','https://rarity.tools/universalsoldiers','https://rarity.tools/fud-monsters','https://rarity.tools/whelpsnft','https://rarity.tools/vegiemon','https://rarity.tools/plodding-pirates','https://rarity.tools/deaddudeproject','https://rarity.tools/maestropups-1','https://rarity.tools/poshpandas','https://rarity.tools/thetigersguild','https://rarity.tools/cryptinies','https://rarity.tools/catctus','https://rarity.tools/barn-owlz-dino-palz','https://rarity.tools/thesingularityheroes','https://rarity.tools/ucac','https://rarity.tools/art-stars-1','https://rarity.tools/tradesquads','https://rarity.tools/song-a-day','https://rarity.tools/kneecaps','https://rarity.tools/meowbits-collection','https://rarity.tools/axie','https://rarity.tools/realcryptopunks-by-vt3-com','https://rarity.tools/chihuahua-gang-revenge','https://rarity.tools/caninecountryclub','https://rarity.tools/monkeybrix','https://rarity.tools/mojibots','https://rarity.tools/dapper-space-collective','https://rarity.tools/direwolvesv2','https://rarity.tools/thevisitors','https://rarity.tools/zales-i-v2-2','https://rarity.tools/nftokins']
for url in urls:
    try:
        msema(url)
    except:
        iko.append(url)
        print(url)
