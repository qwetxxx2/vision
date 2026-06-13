import matplotlib.pyplot as plt


class Chart:

    @staticmethod
    def create_chart(counts):

        names = list(counts.keys())
        values = list(counts.values())

        plt.figure(figsize=(12, 6))

        plt.bar(names, values)

        plt.title("Статистика обнаруженных объектов")
        plt.xlabel("Тип объекта")
        plt.ylabel("Количество")

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.savefig(
            "results/chart.png",
            dpi=150,
            bbox_inches="tight"
        )

        plt.close()