import matplotlib.pyplot as plt

class BotResult:
    def __init__(self, name, color, value):
        self.name = name
        self.color = color
        self.value = value

def create_bar_chart(bot_results, output_file):
    names = [bot.name for bot in bot_results]
    colors = [bot.color for bot in bot_results]
    values = [bot.value for bot in bot_results]

    plt.bar(names, values, color=colors)
    plt.xlabel('Bot Names')
    plt.ylabel('Values')
    plt.title('Bot Results Bar Chart')
    plt.savefig(output_file)
    plt.show()

bot1 = BotResult(name="sagebot", color="blue", value=1000)
bot2 = BotResult(name="RemBot", color="red", value=60)
bot3 = BotResult(name="PaceBot", color="purple", value=400)
bot4 = BotResult(name="Merabot", color="yellow", value=30)
bot5 = BotResult(name="RageBot", color="pink", value=100)

output_file_path = "bot_results_chart.png"
bot_results_list = [bot1, bot2, bot3, bot4, bot5]
create_bar_chart(bot_results_list, output_file_path)
