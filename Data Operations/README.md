Öncelikle *check_format* fonksiyonunda verilen dataset'in "csv" ya da "json" uzatılı olup olmadığını kontrol etmesi için oluşturdum.
Bu fonksiyonda kullanıcı filedata parametresine gönderdiğini veri seti ismi üzerinden json-csv ye karar verip bu veri setlerini dataframe çevirip işleme alacak.


*check_set* fonksiyonunda eğer kullanıcı herhangi bir veri seti atamassa fonsiyon random numpy array oluşturup bunu dataframe'e çevirecek.(Bu kontrolü check_format içinde kullanmaya çalıştım ama nededini anlamadığım şekilde diğer if else'lerim çalışmamaya başladı :D O sebeple ayrı bir fonksiyonda kontrol ettim)

*Des, null_values, corr* fonksiyonlarında veri hakkında detaylı bilgiler almak için küçük çaplı bir analiz elde etmek için oluşturuldu.

*datavisual* fonksiyonunda gönderilen veri seti üzerinden görselleştirme yapacak iki farklı görselleştirme tekniği kullandım. Bu koda gönderilen veri setinin "HolywoodMovies.csv" olduğunu varsayarak görselleştirmeler yapıldı.

-formula1.json uzantılı veri seti kodu kontrol etmek için ayrı olarak oluşturdum.


Ödevi yaparken pythonda class mantığını unuttuğumu fark ettim, unuttuklarımı pekiştirmek için güzel bir ödevdi umarım doğru yapabilmişimdir :)

Yol gösterici tüm geri bildirimler için şimdiden çok teşekkür ederim.

(P.S: Eğer kodu okurken küçük bir akıl tutulması yaşadıysanız özürlerimi bir borç bilin!)
