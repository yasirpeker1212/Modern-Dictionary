meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "BTW" : "Bu arada",
            "GG" : "İyi oyundu",
            "BYE" : "Bay bay",
            "EZ" : "Kolay",
            "AFK" : "klavyeden uzak"
            }
while(1):
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    if word == "çıkış":
        break
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Böyle kelime yok.Ama kelime ekleyebilirsiniz.")
        word_to_add = input("Eklenecek Kelime:")
        word_meaning = input("Ve anlamı:")
        meme_dict[word_to_add] = word_meaning
