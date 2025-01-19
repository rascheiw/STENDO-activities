import streamlit as st
import matplotlib.pyplot as plt
import datetime


def Liste_des_clients_non_rentables(df):
    days = st.selectbox("Nombre de jours", [7, 14, 30, 90, 365, 'depuis la première utilisation'])
    if days == 7:
        st.write(f"{len( df[df['activity_per_day_7_days'] < 1.25][['full_name.1', 'activity_per_day_7_days']].sort_values(by=['activity_per_day_7_days'], ascending=False).rename(columns={'full_name.1' : 'Nom du client','activity_per_day_7_days': 'Nombre moyen séance par jours sur les 7 derniers jours'}))} clients sur {len(df[df['number_days'] > 7])} ne sont pas rentables sur les 7 derniers jours")
        st.dataframe( df[df['activity_per_day_7_days'] < 1.25][['full_name.1', 'activity_per_day_7_days']].sort_values(by=['activity_per_day_7_days'], ascending=False).rename(columns={'full_name.1' : 'Nom du client','activity_per_day_7_days': 'Nombre moyen séance par jours sur les 7 derniers jours'}).style.format({"Nombre moyen séance par jours sur les 7 derniers jours": "{:.2f}"}).hide_index())
    elif days == 14:
        st.write(f"{len( df[df['activity_per_day_14_days'] < 1.25][['full_name.1', 'activity_per_day_14_days']].sort_values(by=['activity_per_day_14_days'], ascending=False).rename(columns={'full_name.1' : 'Nom du client','activity_per_day_14_days': 'Nombre moyen séance par jours sur les 14 derniers jours'}))} clients sur {len(df[df['number_days'] > 14])} ne sont pas rentables sur les 14 derniers jours")
        st.dataframe( df[df['activity_per_day_14_days'] < 1.25][['full_name.1', 'activity_per_day_14_days']].sort_values(by=['activity_per_day_14_days'], ascending=False).rename(columns={'full_name.1' : 'Nom du client','activity_per_day_14_days': 'Nombre moyen séance par jours sur les 14 derniers jours'}).style.format({"Nombre moyen séance par jours sur les 14 derniers jours": "{:.2f}"}).hide_index())
    elif days == 30:
        st.write(f"{len( df[df['activity_per_day_30_days'] < 1.25][['full_name.1', 'activity_per_day_30_days']].sort_values(by=['activity_per_day_30_days'], ascending=False).rename(columns={'full_name.1' : 'Nom du client','activity_per_day_30_days': 'Nombre moyen séance par jours sur les 30 derniers jours'}))} clients sur {len(df[df['number_days'] > 30])} ne sont pas rentables sur les 30 derniers jours")
        st.dataframe( df[df['activity_per_day_30_days'] < 1.25][['full_name.1', 'activity_per_day_30_days']].sort_values(by=['activity_per_day_30_days'], ascending=False).rename(columns={'full_name.1' : 'Nom du client','activity_per_day_30_days': 'Nombre moyen séance par jours sur les 30 derniers jours'}).style.format({"Nombre moyen séance par jours sur les 30 derniers jours": "{:.2f}"}).hide_index())
    elif days == 90:
        st.write(f"{len( df[df['activity_per_day_90_days'] < 1.25][['full_name.1', 'activity_per_day_90_days']].sort_values(by=['activity_per_day_90_days'], ascending=False).rename(columns={'full_name.1' : 'Nom du client','activity_per_day_90_days': 'Nombre moyen séance par jours sur les 90 derniers jours'}))} clients sur {len(df[df['number_days'] > 90])} ne sont pas rentables sur les 90 derniers jours")
        st.dataframe( df[df['activity_per_day_90_days'] < 1.25][['full_name.1', 'activity_per_day_90_days']].sort_values(by=['activity_per_day_90_days'], ascending=False).rename(columns={'full_name.1' : 'Nom du client','activity_per_day_90_days': 'Nombre moyen séance par jours sur les 90 derniers jours'}).style.format({"Nombre moyen séance par jours sur les 90 derniers jours": "{:.2f}"}).hide_index())
    elif days == 365:
        st.write(f"{len( df[df['activity_per_day_year'] < 1.25][['full_name.1', 'activity_per_day_year']].sort_values(by=['activity_per_day_year'], ascending=False).rename(columns={'full_name.1' : 'Nom du client','activity_per_day_year': 'Nombre moyen séance par jours sur 1 an'}))} clients sur {len(df[df['number_days'] > 365])} ne sont pas rentables sur 1 an")
        st.dataframe( df[df['activity_per_day_year'] < 1.25][['full_name.1', 'activity_per_day_year']].sort_values(by=['activity_per_day_year'], ascending=False).rename(columns={'full_name.1' : 'Nom du client','activity_per_day_year': 'Nombre moyen séance par jours sur 1 an'}).style.format({"Nombre moyen séance par jours sur 1 an": "{:.2f}"}).hide_index())
    elif days == 'depuis la première utilisation':
        st.write(f"{len( df[df['activity_per_day_since_acquisition'] < 0.87][['full_name.1', 'activity_per_day_since_acquisition']].sort_values(by=['activity_per_day_since_acquisition'], ascending=False).rename(columns={'full_name.1' : 'Nom du client','activity_per_day_since_acquisition': 'Nombre moyen séance par jours depuis la première utilisation'}))} clients sur {len(df)} ne sont pas rentables")
        st.dataframe( df[df['activity_per_day_since_acquisition'] < 0.87][['full_name.1', 'activity_per_day_since_acquisition']].sort_values(by=['activity_per_day_since_acquisition'], ascending=False).rename(columns={'full_name.1' : 'Nom du client','activity_per_day_since_acquisition': 'Nombre moyen séance par jours depuis la première utilisation'}).style.format({"Nombre moyen séance par jours depuis la première utilisation": "{:.2f}"}).hide_index())

def classement_nombre_moyen_par_jour(df):
    days = st.selectbox("Nombre de jours", [7, 14, 30, 90, 365, 'depuis la première utilisation'])
    if days == 7:
        display_30_best_clients_activity_per_days_7_days = df[df['number_days'] > 7][['full_name.1', 'activity_per_day_7_days', 'rank_activity_per_day_7_days']].sort_values(by=['activity_per_day_7_days'], ascending=False)
        display_30_best_clients_activity_per_days_7_days = display_30_best_clients_activity_per_days_7_days.rename(columns={'full_name.1' : 'Nom du client', 'activity_per_day_7_days': 'Nombre moyen séances par jours sur les 7 derniers jours', 'rank_activity_per_day_7_days' : 'Classement en fonction de l\'activité sur les 7 derniers jours'})
        st.dataframe(display_30_best_clients_activity_per_days_7_days.head(30).style.format({"Nombre moyen séances par jours sur les 7 derniers jours": "{:.1f}"}).hide(axis='index'))
        plt.figure(figsize=(10, 6))
        plt.scatter(display_30_best_clients_activity_per_days_7_days.head(30)['Nom du client'], display_30_best_clients_activity_per_days_7_days.head(30)['Nombre moyen séances par jours sur les 7 derniers jours'], alpha=0.7)
        plt.xlabel('Nom du client')
        plt.ylabel('Nombres moyen de séances par jours')
        plt.title('Classement des 30 premiers clients européens en fonction du nombre moyen de séances par jour sur les 7 derniers jours')
        plt.xticks(rotation=90)
        st.pyplot(plt)
    elif days == 14:
        display_30_best_clients_activity_per_days_14_days = df[df['number_days'] > 14][['full_name.1', 'activity_per_day_14_days', 'rank_activity_per_day_14_days']].sort_values(by=['activity_per_day_14_days'], ascending=False)
        display_30_best_clients_activity_per_days_14_days = display_30_best_clients_activity_per_days_14_days.rename(columns={'full_name.1' : 'Nom du client','activity_per_day_14_days': 'Nombre moyen séances par jours sur les 14 derniers jours','rank_activity_per_day_14_days' : 'Classement en fonction de l\'activité sur les 14 derniers jours'})
        st.dataframe(display_30_best_clients_activity_per_days_14_days.head(30).style.format({"Nombre moyen séances par jours sur les 14 derniers jours": "{:.1f}"}).hide(axis='index'))
        plt.figure(figsize=(10, 6))
        plt.scatter(display_30_best_clients_activity_per_days_14_days.head(30)['Nom du client'], display_30_best_clients_activity_per_days_14_days.head(30)['Nombre moyen séances par jours sur les 14 derniers jours'],  alpha=0.7)
        plt.xlabel('Nom du client')
        plt.ylabel('Nombres moyen de séances par jours')
        plt.title('Classement des 30 premiers clients européens en fonction du nombre moyen de séances par jour sur les 14 derniers jours')
        plt.xticks(rotation=90)
        st.pyplot(plt)
    elif days == 30:
        display_30_best_clients_activity_per_days_30_days = df[df['number_days'] > 30][['full_name.1', 'activity_per_day_30_days', 'rank_activity_per_day_30_days']].sort_values(by=['activity_per_day_30_days'], ascending=False)
        display_30_best_clients_activity_per_days_30_days = display_30_best_clients_activity_per_days_30_days.rename(columns={'full_name.1' : 'Nom du client','activity_per_day_30_days': 'Nombre moyen séances par jours sur les 30 derniers jours', 'rank_activity_per_day_30_days' : 'Classement en fonction de l\'activité sur les 30 derniers jours'})
        st.dataframe(display_30_best_clients_activity_per_days_30_days.head(30).style.format({"Nombre moyen séances par jours sur les 30 derniers jours": "{:.1f}"}).hide(axis='index'))
        plt.figure(figsize=(10, 6))
        plt.scatter(display_30_best_clients_activity_per_days_30_days.head(30)['Nom du client'], display_30_best_clients_activity_per_days_30_days.head(30)['Nombre moyen séances par jours sur les 30 derniers jours'],  alpha=0.7)
        plt.xlabel('Nom du client')
        plt.ylabel('Nombres moyen de séances par jours')
        plt.title('Classement des 30 premiers clients européens en fonction du nombre moyen de séances par jour sur les 30 derniers jours')
        plt.xticks(rotation=90)
        st.pyplot(plt)
    elif days == 90:
        display_30_best_clients_activity_per_days_90_days = df[df['number_days'] > 90][['full_name.1', 'activity_per_day_90_days', 'rank_activity_per_day_90_days']].sort_values(by=['activity_per_day_90_days'], ascending=False)
        display_30_best_clients_activity_per_days_90_days = display_30_best_clients_activity_per_days_90_days.rename(columns={'full_name.1' : 'Nom du client', 'activity_per_day_90_days': 'Nombre moyen séances par jours sur les 90 derniers jours', 'rank_activity_per_day_90_days' : 'Classement en fonction de l\'activité sur les 90 derniers jours'})
        st.dataframe(display_30_best_clients_activity_per_days_90_days.head(30).style.format({"Nombre moyen séances par jours sur les 90 derniers jours": "{:.1f}"}).hide(axis='index'))
        plt.figure(figsize=(10, 6))
        plt.scatter(display_30_best_clients_activity_per_days_90_days.head(30)['Nom du client'], display_30_best_clients_activity_per_days_90_days.head(30)['Nombre moyen séances par jours sur les 90 derniers jours'],  alpha=0.7)
        plt.xlabel('Nom du client')
        plt.ylabel('Nombres moyen de séances par jours')
        plt.title('Classement des 30 premiers clients européens en fonction du nombre moyen de séances par jour sur les 90 derniers jours')
        plt.xticks(rotation=90)
        st.pyplot(plt)
    elif days == 365:
        display_30_best_clients_activity_per_days_year = df[df['number_days'] > 365][['full_name.1', 'activity_per_day_year', 'rank_activity_per_day_year']].sort_values(by=['activity_per_day_year'], ascending=False)
        display_30_best_clients_activity_per_days_year = display_30_best_clients_activity_per_days_year.rename(columns={'full_name.1' : 'Nom du client', 'activity_per_day_year': 'Nombre moyen séances par jours sur 1 an', 'rank_activity_per_day_year' : 'Classement en fonction de l\'activité sur 1 an'})
        st.dataframe(display_30_best_clients_activity_per_days_year.head(30).style.format({"Nombre moyen séances par jours sur 1 an": "{:.1f}"}).hide(axis='index'))
        plt.figure(figsize=(10, 6))
        plt.scatter(display_30_best_clients_activity_per_days_year.head(30)['Nom du client'], display_30_best_clients_activity_per_days_year.head(30)['Nombre moyen séances par jours sur 1 an'],  alpha=0.7)
        plt.xlabel('Nom du client')
        plt.ylabel('Nombres moyen de séances par jours')
        plt.title('Classement des 30 premiers clients européens en fonction du nombre moyen de séances par jour sur 1 an')
        plt.xticks(rotation=90)
        st.pyplot(plt)    
    elif days == 'depuis la première utilisation':
        display_30_best_clients_activity_per_days_entire_period = df[['full_name.1', 'activity_per_day_since_acquisition', 'rank_activity_per_day_since_acquisition']].sort_values(by=['activity_per_day_since_acquisition'], ascending=False)
        display_30_best_clients_activity_per_days_entire_period = display_30_best_clients_activity_per_days_entire_period.rename(columns={'full_name.1' : 'Nom du client', 'activity_per_day_since_acquisition': 'Nombre moyen séance par jours depuis la première utilisation', 'rank_activity_per_day_since_acquisition' : 'Classement en fonction de l\'activité depuis la première utilisation'})
        st.dataframe(display_30_best_clients_activity_per_days_entire_period.head(30).style.format({"Nombre moyen séance par jours depuis acquisition": "{:.1f}"}).hide(axis='index'))
        plt.figure(figsize=(10, 6))
        plt.scatter(display_30_best_clients_activity_per_days_entire_period.head(30)['Nom du client'], display_30_best_clients_activity_per_days_entire_period.head(30)['Nombre moyen séance par jours depuis la première utilisation'],  alpha=0.7)
        plt.xlabel('Nom du client')
        plt.ylabel('Nombres moyen de séances par jours')
        plt.title('Classement des 30 premiers clients européens en fonction du nombre moyen de séances par jour depuis l\'acquisition de l\'appareil V4')
        plt.xticks(rotation=90)
        st.pyplot(plt)

def classement_nombre_par_jour(df):
    days = st.selectbox("Nombre de jours", [7, 14, 30, 90, 365, 'depuis la première utilisation'])
    if days == 7:
        display_30_best_clients_activity_7_days = df[df['number_days'] > 7][['full_name.1', 'activity_last_7_days', 'rank_activity_7_days']].sort_values(by=['activity_last_7_days'], ascending=False)
        display_30_best_clients_activity_7_days = display_30_best_clients_activity_7_days.rename(columns={'full_name.1' : 'Nom du client', 'activity_last_7_days': 'Nombre de séances sur les 7 derniers jours', 'rank_activity_7_days' : 'Classement en fonction de l\'activité sur les 7 derniers jours'})
        st.dataframe(display_30_best_clients_activity_7_days.head(30).style.hide(axis='index'))
        plt.figure(figsize=(10, 6))
        plt.scatter(display_30_best_clients_activity_7_days.head(30)['Nom du client'], display_30_best_clients_activity_7_days.head(30)['Nombre de séances sur les 7 derniers jours'], alpha=0.7)
        plt.xlabel('Nom du client')
        plt.ylabel('Nombres de séances par jours')
        plt.title('Classement des 30 clients européens avec le plus de séances sur les 7 derniers jours')
        plt.xticks(rotation=90)
        st.pyplot(plt)
    elif days == 14:
        display_30_best_clients_activity_14_days = df[df['number_days'] > 14][['full_name.1', 'activity_last_14_days', 'rank_activity_14_days']].sort_values(by=['activity_last_14_days'], ascending=False)
        display_30_best_clients_activity_14_days = display_30_best_clients_activity_14_days.rename(columns={'full_name.1' : 'Nom du client', 'activity_last_14_days': 'Nombre de séances sur les 14 derniers jours', 'rank_activity_14_days' : 'Classement en fonction de l\'activité sur les 14 derniers jours'})
        st.dataframe(display_30_best_clients_activity_14_days.head(30).style.hide(axis='index'))
        plt.figure(figsize=(10, 6))
        plt.scatter(display_30_best_clients_activity_14_days.head(30)['Nom du client'], display_30_best_clients_activity_14_days.head(30)['Nombre de séances sur les 14 derniers jours'], alpha=0.7)
        plt.xlabel('Nom du client')
        plt.ylabel('Nombres de séances par jours')
        plt.title('Classement des 30 clients européens avec le plus de séances sur les 14 derniers jours')
        plt.xticks(rotation=90)
        st.pyplot(plt)
    elif days == 30:
        display_30_best_clients_activity_30_days = df[df['number_days'] > 30][['full_name.1', 'activity_last_30_days', 'rank_activity_30_days']].sort_values(by=['activity_last_30_days'], ascending=False)
        display_30_best_clients_activity_30_days = display_30_best_clients_activity_30_days.rename(columns={'full_name.1' : 'Nom du client', 'activity_last_30_days': 'Nombre de séances sur les 30 derniers jours', 'rank_activity_30_days' : 'Classement en fonction de l\'activité sur les 30 derniers jours'})
        st.dataframe(display_30_best_clients_activity_30_days.head(30).style.hide(axis='index'))
        plt.figure(figsize=(10, 6))
        plt.scatter(display_30_best_clients_activity_30_days.head(30)['Nom du client'], display_30_best_clients_activity_30_days.head(30)['Nombre de séances sur les 30 derniers jours'], alpha=0.7)
        plt.xlabel('Nom du client')
        plt.ylabel('Nombres de séances par jours')
        plt.title('Classement des 30 clients européens avec le plus de séances sur les 30 derniers jours')
        plt.xticks(rotation=90)
        st.pyplot(plt)
    elif days == 90:
        display_30_best_clients_activity_90_days = df[df['number_days'] > 90][['full_name.1', 'activity_last_90_days', 'rank_activity_90_days']].sort_values(by=['activity_last_90_days'], ascending=False)
        display_30_best_clients_activity_90_days = display_30_best_clients_activity_90_days.rename(columns={'full_name.1' : 'Nom du client', 'activity_last_90_days': 'Nombre de séances sur les 90 derniers jours', 'rank_activity_90_days' : 'Classement en fonction de l\'activité sur les 90 derniers jours'})
        st.dataframe(display_30_best_clients_activity_90_days.head(30).style.hide(axis='index'))
        plt.figure(figsize=(10, 6))
        plt.scatter(display_30_best_clients_activity_90_days.head(30)['Nom du client'], display_30_best_clients_activity_90_days.head(30)['Nombre de séances sur les 90 derniers jours'], alpha=0.7)
        plt.xlabel('Nom du client')
        plt.ylabel('Nombres de séances par jours')
        plt.title('Classement des 30 clients européens avec le plus de séances sur les 90 derniers jours')
        plt.xticks(rotation=90)
        st.pyplot(plt)
    elif days == 365:
        display_30_best_clients_activity_year = df[df['number_days'] > 365][['full_name.1', 'activity_last_365_days', 'rank_activity_year']].sort_values(by=['activity_last_365_days'], ascending=False)
        display_30_best_clients_activity_year = display_30_best_clients_activity_year.rename(columns={'full_name.1' : 'Nom du client', 'activity_last_365_days': 'Nombre de séances sur 1 an', 'rank_activity_year' : 'Classement en fonction de l\'activité sur 1 an'})
        st.dataframe(display_30_best_clients_activity_year.head(30).style.hide(axis='index'))
        plt.figure(figsize=(10, 6))
        plt.scatter(display_30_best_clients_activity_year.head(30)['Nom du client'], display_30_best_clients_activity_year.head(30)['Nombre de séances sur 1 an'], alpha=0.7)
        plt.xlabel('Nom du client')
        plt.ylabel('Nombres de séances par jours')
        plt.title('Classement des 30 clients européens avec le plus de séances sur 1 an')
        plt.xticks(rotation=90)
    elif days == 'depuis la première utilisation':
        display_30_best_clients_activity_per_days_entire_period = df[['full_name.1', 'counts', 'rank_activity_since_acquisition']].sort_values(by=['counts'], ascending=False)
        display_30_best_clients_activity_per_days_entire_period = display_30_best_clients_activity_per_days_entire_period.rename(columns={'full_name.1' : 'Nom du client', 'counts': 'Nombre de séances depuis la première utilisation', 'rank_activity_since_acquisition' : 'Classement en fonction de l\'activité depuis la première utilisation'})
        st.dataframe(display_30_best_clients_activity_per_days_entire_period.head(30).style.format({"Nombre de séances depuis la première utilisation": "{:.1f}"}).hide(axis='index'))
        plt.figure(figsize=(10, 6))
        plt.scatter(display_30_best_clients_activity_per_days_entire_period.head(30)['Nom du client'], display_30_best_clients_activity_per_days_entire_period.head(30)['Nombre de séances depuis la première utilisation'],  alpha=0.7)
        plt.xlabel('Nom du client')
        plt.ylabel('Nombre de séances depuis la première utilisation')
        plt.title('Classement des 30 premiers clients européens en fonction du nombre de séances depuis l\'acquisition de l\'appareil V4')
        plt.xticks(rotation=90)
        st.pyplot(plt)

def statistiques_par_clients(df):
    user = st.selectbox("Nom du client", df['full_name.1'].unique())
    target_activity = df[df['full_name.1'] == str(user)]
    if not target_activity.empty:
        current_date = datetime.date.today()
        rank = target_activity['rank_activity_since_acquisition'].iloc[0]
        rank_per_day = target_activity['rank_activity_per_day_since_acquisition'].iloc[0]
        counts = target_activity['counts'].iloc[0]
        activity_per_day = target_activity['activity_per_day_since_acquisition'].iloc[0]
        first_activity = target_activity['first_activity'].iloc[0]
        last_activity = target_activity['last_activity'].iloc[0]
        since_asquisition = target_activity['formatted_duration'].iloc[0]
        days_since_acquisition = target_activity['number_days'].iloc[0]
        activity_last_7_days = target_activity['activity_last_7_days'].iloc[0]
        activity_per_day_last_week = target_activity['activity_per_day_7_days'].iloc[0]
        rank_last_week = target_activity['rank_activity_7_days'].iloc[0]
        activity_last_14_days = target_activity['activity_last_14_days'].iloc[0]
        activity_per_day_last_2_week = target_activity['activity_per_day_14_days'].iloc[0]
        rank_last_2_week = target_activity['rank_activity_14_days'].iloc[0]
        activity_last_30_days = target_activity['activity_last_30_days'].iloc[0]
        activity_per_day_last_30_days = target_activity['activity_per_day_30_days'].iloc[0]
        rank_last_30_days = target_activity['rank_activity_30_days'].iloc[0]
        activity_last_90_days = target_activity['activity_last_90_days'].iloc[0]
        activity_per_day_last_90_days = target_activity['activity_per_day_90_days'].iloc[0]
        rank_last_90_days = target_activity['rank_activity_90_days'].iloc[0]
        activity_last_365_days = target_activity['activity_last_365_days'].iloc[0]
        activity_per_day_last_year = target_activity['activity_per_day_year'].iloc[0]
        rank_last_year = target_activity['rank_activity_year'].iloc[0]

        st.markdown(f"**__Détail pour le client {user}:__**")
        st.write("\n")
        st.write(f"Date d\'aujourd\'hui: {current_date}")
        st.write(f"Date de la première séance: {first_activity}")
        st.write(f"Date de la dernière séance: {last_activity}")
        st.write(f"Première utilisation il y a: {since_asquisition} (ou {days_since_acquisition} jours)")
        st.write("\n")

        st.markdown("**__Stats sur les 7 derniers jours__**")
        if target_activity['number_days'].iloc[0] < 7:
            st.write("Première séance effectué il ya moins de 7 jours.")
        st.write(f"Nombres de séances: {activity_last_7_days}")
        st.write(f"Nombres de séances par jour: {activity_per_day_last_week}")
        st.write(f"Classement: {rank_last_week} ")

        st.write("\n")
        st.markdown("**__Stats sur les 14 derniers jours__**")
        if target_activity['number_days'].iloc[0] < 14:
            st.write("Première séance effectué il ya moins de 14 jours.")
        st.write(f"Nombres de séances: {activity_last_14_days}")
        st.write(f"Nombres de séances par jour: {activity_per_day_last_2_week}")
        st.write(f"Classement: {rank_last_2_week}")

        st.write("\n")
        st.markdown("**__Stats sur les 30 derniers jours__**")
        if target_activity['number_days'].iloc[0] < 30:
            st.write("Première séance effectué il ya moins de 30 jours.")
        st.write(f"Nombres de séances: {activity_last_30_days}")
        st.write(f"Nombres de séances par jour: {activity_per_day_last_30_days}")
        st.write(f"Classement: {rank_last_30_days}")
        st.write("\n")

        st.markdown("**__Stats sur les 90 derniers jours__**")
        if target_activity['number_days'].iloc[0] < 90:
            st.write("Première séance effectué il ya moins de 90 jours.")
        st.write(f"Nombres de séances: {activity_last_90_days}")
        st.write(f"Nombres de séances par jour: {activity_per_day_last_90_days}")
        st.write(f"Classement: {rank_last_90_days}")

        st.write("\n")
        st.markdown("**__Stats sur 1 an__**")
        if target_activity['number_days'].iloc[0] < 365:
            st.write("Première séance effectué il ya moins de 365 jours.")
        st.write(f"Nombres de séances: {activity_last_365_days}")
        st.write(f"Nombres de séances par jour: {activity_per_day_last_year}")
        st.write(f"Classement: {rank_last_year}")
        st.write("\n")

        st.markdown("**__Stats depuis la première utilisation__**")
        st.write(f"Nombres de séances totales: {counts}")
        st.write(f"Classement: {rank}")
        st.write(f"Nombres moyen de séances par jour: {activity_per_day}")
        st.write(f"Classement: {rank_per_day}")

    else:
        st.write(f"{user} n'existe pas dans la base de données")