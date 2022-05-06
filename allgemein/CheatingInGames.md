# How does cheating works in modern games (*still in progress*)

## What tricks are commonly used to cheat in video games?

Video game cheaters use a wide range of tricks to gain an unfair advantage. Here are the most popular forms of cheating:

- ***Aim Bots*** ensure cheaters automatically have perfect aim at any opponent.
- ***Trigger Bots*** cause the cheater’s weapons to automatically fire when their target is in the crosshairs.
- ***Wall Hacks*** enable cheaters to see hidden threats or targets through walls
- ***Camera Hacks*** give cheaters a wider view of the game world than other players or than the developer intended.
- ***Lag Switches*** delay an opponent’s action, so the cheater has an advantage.
- ***ESP on-screen visuals*** that reveal information to the cheater, such as the cooldown time of enemy abilities or the locations of spawned loot.
- ***Removal*** eliminates challenging elements of the game to make the cheater’s play easier.
- ***Radar*** gives cheaters a map showing the location of opponents, items, power-ups etc.
- ***Unlocking*** gives immediate access to characters, achievements or costumes that must usually be bought or earned.
- ***Drop Hacks and DDOS*** (distributed denial of service) disconnect the cheater just before they lose a game or disconnect opponents to make game play easier.
- ***Boosting/Farming/Stat-Padding*** artificially boost win rates and rankings by using fake accounts or opponents who agree to lose.
- ***Currency Manipulation*** gives cheaters easy access to currency via coin farms while everyone else must earn or buy it.
- ***Scripting*** allows cheaters to automatically respond perfectly and instantly to opponent actions.

## Wir funktionieren Aimbots?
***Color-Aimbots***
Kleine Programme, die zusätzlich zum Spiel im hintergrund laufen. Der Nutzer wählt hier eine bestimmte RGB Farbe als Ziel aus wie zum Beispiel Hautfarbe oder die Farbe einer Uniform und der Bot wertet während des Gameplays die Farben auf dem Bildschirm aus. Wird die ausgewählte Farbe auf dem Bildschirm gefunden, wird automatisch auf das Ziel angelegt.
Nachteil: 
-CPU und GPU müssen 'stark' sein
-Es ist nie auszuschließen, dass die vorgegebene Zielfarbe nicht auch in einer anderen Textur vorkommt (Teammitglieder) 
-nutzloser bei Spielen, die grafisch weit fortgeschritten sind (durch Colorhacks wird die Grafikausgabe angepasst(Modifiezierung Game files))
Vorteil: Keine Game files müssen modifiziert werden -> AntiCHeat Programme erkennen das nicht so schnell (ohne Colorhack)

***Client Hook Aimbots***
Der Spieler erhält tiefgreifenderen Zugriff auf eigentlich verborgende Spielmechaniken -> setzt Modifiezierung von Game files voraus

Mittels sogenannter DLL Injections wird die Exekutive vom Spiel dazugezwungen auch Dateien auszuführen, die nicht zum Spiel gehören. So lassen sich beispielsweise Spielerkoordinaten aus dem Speicher auslesen, die das Spiel dazubenötigt, um andere Spieler an ihren jeweiligen Positionen zu rendern. Jedes Spiel verfügt daher meist über XYZ-Koordinaten aller Spieler einer Session. Danach brauchst man noch simpelste Mathematik, um einen Vektor zwischen Ziel und Spielerposition zu berechnen.

***OpenGL oder DirectX Schnittstellen***

Die aufwendigste Art und Weise ist das Einklinken in OpenGL oder DirectX Schnittstelle. Das Entwenden dieser Informationen gibt dem Nutzer Koordinaten über die Spieler auf dem gesamten Server.
______________
Quellen :
https://blog.irdeto.com/video-gaming/cheating-in-games-everything-you-always-wanted-to-know-about-it/
https://youtu.be/uf41YJPM6SE
