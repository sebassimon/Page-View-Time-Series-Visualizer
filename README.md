<h1>Time Series Visualization</h1>



<h2>Description</h2>
<p>This project visualizes time series data from the freeCodeCamp forum, analyzing daily page views from 2016 to 2019. We use Pandas, Matplotlib, and Seaborn to uncover trends and growth patterns.</p>

<h2>Environments & Tools Used</h2>
<ul>
  <li><b>Python</b></li>
  <li><b>Pandas</b> for data manipulation</li>
  <li><b>Matplotlib</b> and <b>Seaborn</b> for data visualization</li>
</ul>

<h2>Visualization Techniques</h2>

<h3>Bar Chart for Monthly Page Views</h3>
<pre><code>df_grouped.plot(kind='bar')</code></pre>
<img src="https://raw.githubusercontent.com/sebassimon/Page-View-Time-Series-Visualizer/main/bar_plot.png" alt="Bar Chart"/>

<h3>Box Plots for Distribution Analysis</h3>
<pre><code>sns.boxplot(x='month', y='value', data=df_copy)</code></pre>
<img src="https://miro.medium.com/max/720/1*V7c9z9CawePeWgnK9EtTcg.png" alt="Box Plot"/>

<h2>Conclusion</h2>
<p>Through detailed visual analysis, we can better understand the forum's user engagement and identify key growth periods, helping to guide strategic planning.</p>
