# importing pandas and plotly.express
import pandas
import plotly.express as plotlyExp

# <> reading the data and creating dataframe </>
# <> grouping csv with respect to mean of student and level and attempt </>
# <> setting different colors to points on scatter graph by using attempts of the students </>
plotlyExp.scatter(pandas.read_csv("data.csv").groupby(["Student ID", "Level"], as_index=False)["Attempt"].mean(), x="Student ID", y="Level",
                  size="Attempt", color="Attempt").show()
