from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def dashboard():
    return 'Homepage'


@app.route('/dashboard/last_year')
def last_year():
    from bokeh.plotting import figure
    import pandas as pd
    from bokeh.embed import components
    from bokeh.resources import CDN

    df = pd.read_csv('data/new_file.csv', parse_dates=['Date'])
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by='Date')
    p = figure(width=1000, height=500, x_axis_type="datetime")
    p.line(df['Date'], df['Post'], color='red')
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'No. of Post'

    script, div = components(p)
    cdn_js = CDN.js_files[0]

    return render_template('year.html', script=script, div=div, cdn_js=cdn_js)


@app.route('/dashboard/month')
def month():
    from bokeh.plotting import figure
    import pandas as pd
    from bokeh.embed import components
    from bokeh.resources import CDN

    df = pd.read_csv('data/month_data.csv', parse_dates=['Date'])
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by='Date')
    p = figure(width=1000, height=500, x_axis_type="datetime")
    p.line(df['Date'], df['Post'], color='red')
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'No. of Post'

    script, div = components(p)
    cdn_js = CDN.js_files[0]

    return render_template('month.html', script=script, div=div, cdn_js=cdn_js)


@app.route('/dashboard/quarter')
def quarter():
    from bokeh.plotting import figure
    import pandas as pd
    from bokeh.embed import components
    from bokeh.resources import CDN

    df = pd.read_csv('data/quarter.csv', parse_dates=['Date'])
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by='Date')
    p = figure(width=1000, height=500, x_axis_type="datetime")
    p.line(df['Date'], df['Post'], color='red')
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'No. of Post'

    script, div = components(p)
    cdn_js = CDN.js_files[0]

    return render_template('quarter.html', script=script, div=div, cdn_js=cdn_js)


if __name__ == '__main__':
    app.run(debug=True)