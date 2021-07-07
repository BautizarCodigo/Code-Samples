import matplotlib.pyplot as plt
# Import seaborn
import seaborn as sns


class SeabornBasics:

    tips = sns.load_dataset("tips")

    def tips_dataset(self):

        print(self.tips)


    def show_basic_graph(self):

        # Apply the default theme
        sns.set_theme()
        # Create a visualization
        sns.relplot(
            data=tips,
            x="total_bill", y="tip", col="time",
            hue="smoker", style="smoker", size="size",
        )


#plt.show()

if __name__ == "__main__":

    sn = SeabornBasics()
    sn.tips_dataset()