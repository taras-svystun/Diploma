import streamlit as st

def intro():
    import streamlit as st

    st.title('Source separation')
    st.write('Part 2: 93 bpm edition 🤯🔥')
    # st.success("Select a demo above.")

    st.markdown(
        """
        You can choose any of the following:
        
        browse throught the 93 bpm library. It contains:
        1. bass
        2. drums
        3. other instrumentals
        4. vocals

        Each of the aforementioned is extacted using Source Separation Model from 
        the following artists:
        1. A Tribe Called Quest
        2. Notorious B.I.G.
        3. Big L
        4. Bill Withers
        5. Stanley Turrentine
        6. tribe called quest
    """
    )

def samples_library():
    import streamlit as st
    import librosa
    import os
    from glob import glob
    st.title('Original samples library🎵🎧')
    artist_names = [
        'A Tribe Called Quest',
        'Notorious B.I.G.',
        'Big L',
        'Bill Withers',
        'Stanley Turrentine',
        'tribe called quest'
    ]

    artist_option = st.selectbox(
        'Select which artist do you want to hear?',
        artist_names, key=1)

    full_or_sample_option = st.selectbox(
        'Do you prefer a full track or a 20 sec sample?',
        ['full', 'sample'], key=2)

    st.title(' '.join(['You selected:', ':rainbow[' + artist_option + ']', full_or_sample_option, 'recording']))
    filenames = sorted(glob('./soundcloud_tracks_mp3s/93_bpm/*.mp3')) if full_or_sample_option == 'full' \
        else sorted(glob('./soundcloud_tracks_mp3s/93_bpm/*.wav'))
    filename = filenames[artist_names.index(artist_option)]

    recording, sr = librosa.load(filename)
    st.audio(recording, sample_rate=sr)


def sources_library():
    import streamlit as st
    import librosa
    from glob import glob
    st.title('Sources library (bass, drums, other and vocals)🎵🎧')
    artist_names = [
        'A Tribe Called Quest',
        'Notorious B.I.G.',
        'Big L',
        'Bill Withers',
        'Stanley Turrentine',
        'tribe called quest'
    ]


    st.title('Bass🎸🔊🎶🎵👇')
    bass_option = st.selectbox(
        'Select which artist do you want to hear?',
        artist_names, key=3)
    
    st.title(' '.join(['You selected:', ':rainbow[' + bass_option + "'s]", 'bass']))
    filenames = sorted(glob('./soundcloud_tracks_mp3s/93_bpm/*/'))
    bass_filename = filenames[artist_names.index(bass_option)] + 'bass.mp3'

    bass, sr = librosa.load(bass_filename)
    st.audio(bass, sample_rate=sr)






    st.title('Drums🥁🔊🎶🎵🥁')
    drums_option = st.selectbox(
        'Select which artist do you want to hear?',
        artist_names, key=4)
    
    st.title(' '.join(['You selected:', ':rainbow[' + drums_option + "'s]", 'drums']))
    filenames = sorted(glob('./soundcloud_tracks_mp3s/93_bpm/*/'))
    drums_filename = filenames[artist_names.index(drums_option)] + 'drums.mp3'

    drums, sr = librosa.load(drums_filename)
    st.audio(drums, sample_rate=sr)






    st.title('Other🎷🎺🎻🎵🔊')
    other_option = st.selectbox(
        'Select which artist do you want to hear?',
        artist_names, key=5)
    
    st.title(' '.join(['You selected:', ':rainbow[' + other_option + "'s]", 'other']))
    filenames = sorted(glob('./soundcloud_tracks_mp3s/93_bpm/*/'))
    other_filename = filenames[artist_names.index(other_option)] + 'other.mp3'

    other, sr = librosa.load(other_filename)
    st.audio(other, sample_rate=sr)






    st.title('Vocals🎤🎵🔊🗣️🎶')
    vocals_option = st.selectbox(
        'Select which artist do you want to hear?',
        artist_names, key=6)
    
    st.title(' '.join(['You selected:', ':rainbow[' + vocals_option + "'s]", 'vocals']))
    filenames = sorted(glob('./soundcloud_tracks_mp3s/93_bpm/*/'))
    vocals_filename = filenames[artist_names.index(vocals_option)] + 'vocals.mp3'

    vocals, sr = librosa.load(vocals_filename)
    st.audio(vocals, sample_rate=sr)


def mixing():
    import streamlit as st
    import librosa
    from glob import glob
    import soundfile as sf
    artist_names = [
        'A Tribe Called Quest',
        'Notorious B.I.G.',
        'Big L',
        'Bill Withers',
        'Stanley Turrentine',
        'tribe called quest'
    ]
    component_emojies = ['🎸🔊🎶🎵👇', '🥁🔊🎶🎵🥁', '🎷🎺🎻🎵🔊', '🎤🎵🔊🗣️🎶']

    st.title("Mixing")
    st.markdown("""### Hint
It could be challenging during the first time, because some combinations
do not overlap well, however consider the following:
1. 🎸Stanley Turrentine bass, 🎷A Tribe Called Quest other and 🎤tribe called quest vocals
2. 🎸Bill Withers's bass and 🥁tribe called quest's drums
3. 🎸Bill Withers's bass, 🥁tribe called quest's drums, 🎷Bill Withers's other and 🎤Notorious B.I.G.'s vocals 
                """)
    components_names = ['bass', 'drums', 'other', 'vocals']

    col1, col2, col3 = st.columns(3)



    option = st.multiselect(
        'Select desired components',
        components_names, key=7
    )

    if 'clicked' not in st.session_state:
        st.session_state.clicked = False

    def click_button():
        st.session_state.clicked = True

    st.button("I am ready to mixing", on_click=click_button)

    if st.session_state.clicked:
        full_name = []

        mix = 0
        idx = 5
        mix_ingredients = []

        for component in option:
            idx += 1
            st.title(component + component_emojies[components_names.index(component)])
            artist_option = st.selectbox(
                'Select which artist do you want to hear?',
                artist_names, key=7+idx)
            
            st.markdown('#### ' + ' '.join(['You selected:', ':rainbow[' + artist_option + "'s]", component]))
            full_name.append(artist_option + ' ' + component)
            filenames = sorted(glob(f'./soundcloud_tracks_mp3s/93_bpm/*/{component}.mp3'))
            filename = filenames[artist_names.index(artist_option)]

            sample, sr = librosa.load(filename)
            mix_ingredients.append(sample[:452160])
            st.audio(sample, sample_rate=sr)

            mix += sample[:452160]


        if st.button("Mix!", type="primary"):
            mix = sum(mix_ingredients)

            st.write('Enjoy here! (It already saved to your computer)')
            mix_name = f'mixes/{" + ".join(full_name)}.wav'
            sf.write(mix_name, mix, sr, 'PCM_24')
            st.audio(mix, sample_rate=sr)
            

page_names_to_funcs = {
    "Welcome page": intro,
    "Original samples library": samples_library,
    "Sources library (bass, drums, other and vocals)": sources_library,
    "Mixing": mixing
}

st.write("# Welcome to my Sampling Heaven and Mixing Service👋!")
st.write("It is a welcome page. I invite you to visit library of mixing pages!")
demo_name = st.selectbox(
    "Select one",
    page_names_to_funcs.keys()
)

page_names_to_funcs[demo_name]()