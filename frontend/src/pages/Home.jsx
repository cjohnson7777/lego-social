import { Theme } from "../components/SetDetails";
import { useState, useEffect } from 'react'


function Home(){
  const key = '012535ebae0227cee00bc3205c83f64c'; 
  const themeurl = 'https://rebrickable.com/api/v3/lego/themes/'
  const url = 'https://rebrickable.com/api/v3/lego/sets/?min_parts=2014'

  const [sets, setSets] = useState({});
  const [themes, setThemes] = useState({})

  useEffect(() => { 
    const fetchSetsAndThemes = async () => {
      try {
        const setsResponse = await fetch(`${url}&key=${key}`);
        const setsData = await setsResponse.json();

        const themesResponse = await fetch(`${themeurl}?key=${key}`);
        const themesData = await themesResponse.json();

        const themeMap = {};
        themesData.results.forEach(theme => {
            themeMap[theme.id] = theme.name;
        });

        const setsByTheme = {};
        setsData.results.forEach(set => {
            const themeId = set.theme_id;
            if (!setsByTheme[themeId]) {
                setsByTheme[themeId] = [];
            }
            setsByTheme[themeId].push(set);
        });

        setThemes(themeMap)
        setSets(setsByTheme);
      } catch (error) {
        console.error("Error fetching sets:", error);
      }
    };

    fetchSetsAndThemes();
  }, []);

    return (
        <div>
            {Object.keys(sets).map((themeId, i) => (
                <Theme key={i} themeName={themes[themeId] || "Unspecified"} sets={sets[themeId]}/>
            ))}
        </div>
    )
}

export default Home;