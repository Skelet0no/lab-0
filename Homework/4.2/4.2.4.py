def month(num, lang="ru"):
    months = {
        1: ["Яанварь", "January"],
        2: ["Февраль", "February"],
        3: ["Март", "March"],
        4: ["Апрель", "April"],
        5: ["Май", "May"],
        6: ["Июнь", "June"],
        7: ["Июль", "July"],
        8: ["Август", "August"],
        9: ["Сентябрь", "September"],
        10: ["Октябрь", "October"],
        11: ["Ноябрь", "November"],
        12: ["Декабрь", "December"]
    }
    return months[num][0] if lang == "ru" else months[num][1]
