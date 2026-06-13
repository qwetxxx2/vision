class Statistics:

    @staticmethod
    def get_counts(results):

        counts = {}

        for result in results:
            for box in result.boxes:

                cls = int(box.cls[0])

                name = result.names[cls]

                counts[name] = counts.get(name, 0) + 1

        return dict(
            sorted(
                counts.items(),
                key=lambda x: x[1],
                reverse=True
            )
        )

    @staticmethod
    def save_statistics(counts, filename):

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                "Статистика объектов\n\n"
            )

            for name, count in counts.items():
                file.write(
                    f"{name}: {count}\n"
                )