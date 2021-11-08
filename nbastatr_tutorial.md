# Get NBA dataset in R

Yanbing Chen

## Motivation

My final project for this course is analysis on professional basketball, more specifically, the transformation of game style of professional basketball. Having a great dataset is a prerequisite for the project but the official dataset is only viewable on NBA.com but not available for downloading as csv file. Fortunately, there is a useful package in R called 'nbastatR'. Hence, while I am trying to explore the package in R, it is also great to complete this tutorial to share the information and help others who are also interested in NBA or basketball analysis in R.

The thing needed to be noticed that the package might not satisfy your all needs for the project. There are other ways to obtain the data, such as scraping data from NBA official website using python, which I am also investing on.

Since there are a lot of functions in the package to use, I will mainly focus on the functions related to my topic. For more information, please refer to  https://www.rdocumentation.org/packages/nbastatR/versions/0.1.110202031 and the package maintainer Alex Bresler. 

## installation


```r
devtools::install_github("abresler/nbastatR")
library(nbastatR)
```

## Functions

agents_players() Players Agents

all_nba_teams() All NBA Teams

all_star_games() NBA All Star Games

assign_bref_data() Assign nested BREF data to environment

assign_nba_players() Assign NBA player dictionary to environment

assign_nba_teams() Assign NBA teams to environment

beyond_the_numbers() NBA.com Beyond The Numbers Articles

box_scores() NBA box scores

bref_awards() Basketball reference awards

bref_awards_votes() Basketball Reference award votes

bref_bios() Basketball Reference players bios

bref_injuries() Active injuries

bref_players_stats() Basketball Reference Player Season Tables

bref_teams_stats() Basketball Reference teams seasons data

coaching_staffs() NBA active coaching staffs

current_schedule() NBA current season schedule

current_standings() Current standings

days_scores() Get NBA Dates' NBA Scores

dictionary_bref_awards() Basketball Reference Awards

dictionary_bref_coaches() Basketball Reference coach dictionary

dictionary_bref_players() Basketball Reference player dictionary

dictionary_bref_teams() Basketball Reference team dictionary

dictionary_nba_names() Dictionary of NBA Headers and nbastatR names

dictionary_player_photos() Cached player photo dictionary

draft_combines() NBA draft combine data

drafts() NBA drafts

fanduel_summary() Games fanduel summary

franchise_leaders() Franchise leaders

game_logs() NBA game logs for specified parameters

hoops_hype_salary_summary() HoopsHype NBA teams summary salaries

hoopshype_salaries() Hoopshype teams players salaries

metrics_leaders() League leaders by season

nba_franchise_history() Get NBA franchise history

nba_insider_salaries() NBA team salaries

nba_player_ids() Players' NBA player ids

nba_players() NBA player dictionary

nba_stats_api_items() NBA stats API parameters, teams and items

nba_teams() NBA team dictionary

nba_teams_ids() NBA team ids

nba_teams_seasons() NBA teams seasons

nbadraftnet_mock_drafts() NBADraft.net mock drafts

nbastats_api_parameters() NBA Stats API Parameters

play_by_play() NBA games play-by play

play_by_play_v2() NBA games play-by-play v2

player_profiles() NBA.com player profiles

players_agents() Get NBA Players Agents

players_awards() NBA players awards

players_bios() NBA.com bios

players_careers() Player career stats

players_rotowire() Players RotoWire news

players_tables() NBA players table data

playoff_pictures() NBA seasons playoff picture

pst_transaction() ProSports NBA transactions

scale_per_minute() Summarise data per minute

seasons_players() Seasons players

seasons_rosters() NBA teams seasons rosters

seasons_schedule() NBA seasons schedules

sl_players() Summer League Players

sl_teams() Summer League Teams

spread_data() Spread gathered data frame

standings() Get seasons standing data

summarise_per_minute() Summarize data per minute

synergy() Get Synergy data for specified season

team_season_roster() Team roster

teams_annual_stats() NBA teams yearly performance

teams_coaches() Seasons coaching staffs

teams_details() NBA teams details

teams_players_stats() NBA teams and player statistics

teams_rankings() NBA teams rankings

teams_rosters() Teams seasons rosters

teams_rotowire() Teams Rotowire news

teams_seasons_info() NBA teams seasons information

teams_shots() Get teams seasons shot charts

teams_tables() NBA Team table data by season

transactions() NBA transactions since 2012

validate_nba_player_photos() Validate NBA Player photos

widen_bref_data() Widens basketball reference table data

win_probability() NBA games win probabilities


## Guides to Functions

Here are several examples for me to approach the goal of my analysis by using the package.

1. By looking at players drafted in each year, we could figure out what kind of players teams wanted in the past and nowadays.

```r
drafts(draft_years = 2000:2010)
```

2. By looking at total point leader in each season, we could discover how the games are changing, maybe from dominating by centers to guards.

```r
metrics_leaders(seasons = 2000:2010,
                metric = "pts",
                season_types = "Regular Season",
                modes = "PerGame")
```

3. By examining the shot chart, we could find some trends about shooting such as longer shot distance.

```r
teams_shots(teams = "Brooklyn Nets", seasons = 2000:2010)
```

4. By summarizing the total points each season, we might see some changes to the speed of plays in a game.

```r
teams_annual_stats(teams = "New York Knicks",modes = c("Totals"))
```
