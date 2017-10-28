import folium

m = folium.Map(
    location=[-0.94924 100.35427],
    zoom_start=10,
    )
    
 folium.Marker(
    location=[-0.701316, 100.290751],
    popup='Lubuk Alung, Kabupaten Padang Pariaman, Sumatera Barat 25582',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
    
folium.Marker(
    location=[-0.948799, 100.415458],
    popup='Tanah Sirah Piai Nan XX
Lubuk Begalung, Kota Padang, Sumatera Barat',
    icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
    location=[-0.933774, 100.408908],
    popup='Pisang
Pauh, Kota Padang, Sumatera Barat',
    icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
    location=[-0.909745, 100.371485],
    popup='Tabing Banda Gadang
Nanggalo, Kota Padang, Sumatera Barat',
    icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
    location=[-0.891316, 100.408590],
    popup='Gn. Sarik
Kuranji, Kota Padang, Sumatera Barat',
    icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
    location=[-0.434739, 100.329522],
    popup='Kabupaten Tanah Datar
Sumatera Barat',
    icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
    location=[-1.049919, 101.043633],
    popup='Garabak Data
Tigo Lurah Bajanjang, Solok, Sumatera Barat',
    icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
    location=[0.084361, 100.335015],
    popup='Sialang
Kapur IX, Kabupaten Lima Puluh Kota, Sumatera Barat',
    icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
    location=[0.291727, 99.554986],
    popup='Lembah Malintang
Ujung Gading, Kabupaten Pasaman Barat, Sumatera Barat',
    icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
    location=[-0.773922, 100.274590],
    popup='Katapiang
Batang Anai, Kabupaten Padang Pariaman, Sumatera Barat',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
