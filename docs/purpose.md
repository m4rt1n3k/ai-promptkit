# Účel ai-promptkit

## V jedné větě

ai-promptkit má jednomu člověku umožnit řídit hierarchii LLM agentů v několika dlouhodobých projektech aplikovaného výzkumu tak, aby jeho pozornost šla jen na to, co umí jen on, a aby se mezi sezeními, agenty a fázemi projektu nic podstatného neztratilo ani nepřikrášlilo.

## Pro koho a v jaké situaci

- Pro jednoho výzkumníka a inženýra (UCEEB ČVUT, energetika budov), který současně vede několik provázaných repozitářů (`asset-ontology`, `asset-classes`, `asset-runtime`, konektory časových řad, EMO) a k tomu návrhy projektů, zprávy pro TAČR, články a přenos do praxe.
- Pracuje střídavě s různými agenty a nástroji: v devlogu jeho projektů se střídají Cursor Agent, Codex, Composer i Grok. Každé nové sezení začíná s prázdnou pamětí.
- Doménová pravda je křehká: jednotky (kW v konfiguraci, W v databázi), znaménka toků, vlastnictví dat, původ měření. Chyba v nich se z kódu nepozná, projeví se až na budově.

## Co má kit řešit

V historii repa od června do září 2026 se mechanismy několikrát úplně změnily. Potřeby pod nimi zůstaly stejné:

1. **Šetřit lidskou pozornost.** Člověk dodává záměr, úsudek, pravomoc a kontakt s realitou. Vybírání rolí, psaní a kopírování promptů, přenášení výstupů mezi nástroji a pamatování si stavu mají zmizet.
2. **Udržet kontinuitu.** Nový agent v libovolném nástroji naváže bez vysvětlování. Ví, co chceme, co víme, co je rozhodnuté a co čeká na člověka.
3. **Udržet pravdivost.** Každé tvrzení nese stav důkazu (hypotéza, změřeno, ověřeno, vyvráceno) a odkaz na něj. Nic se nevymýšlí a negativní výsledky zůstávají. Stejná tvrzení se pak použijí v návrhu projektu, v článku i ve zprávě pro poskytovatele.
4. **Chránit pravomoc.** Nevratné kroky a kroky navenek (odeslání, publikace, nasazení na reálný objekt, závazek, peníze, kontakt s lidmi) dělá nebo schvaluje člověk. Všechno vratné smějí agenti udělat sami.
5. **Být znovupoužitelný.** Metoda žije na jednom místě, je verzovaná a do projektů se připíná. Zlepšuje se podle skutečných problémů v projektech, ne podle úvah o nich.

## Co kit není

- Není to projektové řízení, issue tracker ani druhý systém specifikací vedle Spec Kitu a gitu.
- Není to sada person, které člověk ručně vyvolává.
- Není to plně autonomní agent. Míru autonomie nastavuje člověk a může ji zvyšovat podle toho, jak se agentům daří.
- Není to popis ideální instituce. Popisuje, co agenti s dostupnými nástroji skutečně umějí.

## Podle čeho poznat, že účel plní

| Kritérium | Cíl |
|-----------|-----|
| Vstup člověka do sezení | pár řádků: záměr, odpovědi, pozorování; žádné kopírování promptů |
| Studený start nového agenta | do 2 minut a bez vysvětlování člověkem |
| Otázka na člověka | dá se zodpovědět do minuty; otevřené jsou nejvýš tři |
| Dohledatelnost | každé tvrzení v článku nebo zprávě má stav a odkaz na důkaz |
| Ztráty | žádné rozhodnutí ani doménový invariant nežije jen v chatu |
| Velikost jádra | člověk ho přečte za 5 minut |
| Skutečné použití | kit běží v projektech, na kterých se právě pracuje |

## Stav k 23. 9. 2026

Principy kit pojmenoval dobře, jako nástroj ale účel neplní. Současnou verzi nepoužívá žádný projekt, člověku práci přidává místo ubírá a kontinuitu, kvůli které kit vznikl, záměrně vypustil. Podrobnosti jsou v [review.md](review.md), návrh řešení v [master.md](master.md).
