# Master — ai-promptkit

<!-- Jediný sdílený stav projektu. Píše vedoucí agent, Záměr píše člověk. Protokol: master/protocol.md. -->

## Rozhodni
<!-- Nejvýš 3. Odpověz za „→“ písmenem nebo větou. -->

1. **Platí navržený Záměr níže?** A) ano · B) ano, se změnami (napiš je) · C) účel je jiný
   Doporučuji A: vychází z historie repa a z toho, co projekty skutečně používají. Bez odpovědi: nic neměním, jen čtu. Podklady: docs/purpose.md
   →
2. **Co má být jádrem kitu?** A) Master; role, DEV|L a Spec Kit jako čočky · B) Master na zkoušku vedle dnešního stavu · C) zůstat u DEV|L a backbone
   Doporučuji B teď a A po pilotu: změna jádra je jednosměrná pro projekty, které kit připínají. Bez odpovědi: stávající soubory zůstávají beze změny. Podklady: docs/review.md, docs/master.md
   →
3. **Kde Master dva týdny zkusit?** A) asset-classes · B) asset-runtime · C) jinde (napiš kde)
   Doporučuji A, nebo projekt, na kterém tento týden pracuješ: asset-classes už má kit jako submodul a testy, které poslouží jako hodnotitel. Bez odpovědi: čekám. Podklady: docs/master.md, oddíl Jak poznáme, že funguje
   →

## Víme
<!-- ? hypotéza · ▶ ověřujeme · ~ zjištěno · ✓ ověřeno · ✗ vyvráceno. Důkaz za „→“. -->

- ~ Současnou verzi kitu nepoužívá žádný projekt; submoduly jsou na 4201e8f a 91afb72 → docs/review.md, oddíl Co ukazuje skutečné použití
- ~ Projekty skutečně udržují devlog, handoff s invarianty a ADR; Spec Kit v team-me má nevyplněnou ústavu a žádnou feature → tamtéž
- ~ Preset chce Spec Kit ≥ 1.0.4, v team-me je 1.0.2 → spec-kit/presets/devl-spiral/preset.yml, team-me/.specify/init-options.json
- ~ Jádro kitu má asi 12 000 slov ve 28 souborech, kaskádu opakuje 16 z nich → docs/review.md, slabé místo 7
- ? Master ušetří člověku práci proti devlogu a handoffu → chybí: pilot
- ▶ Dvoutýdenní pilot Masteru v jednom projektu — ověříme: člověk ≤ 10 min denně, studený start ≤ 2 min, žádné rozhodnutí jen v chatu, check.py bez chyb → čeká na Rozhodni 3

## Záměr
<!-- Návrh agenta 2026-09-23. Platí po potvrzení v Rozhodni 1. -->

Cíl: jeden člověk řídí hierarchii agentů v několika projektech aplikovaného výzkumu a jeho pozornost jde jen na záměr, rozhodnutí a realitu (docs/purpose.md).
Hotovo, když: kit běží aspoň ve dvou aktivních projektech a splňuje kritéria v docs/purpose.md.
Agenti smí sami: číst, psát a upravovat soubory kitu v pracovní větvi, rešerše, návrhy.
Vždy se mě zeptej: commit a push do main, změna jádra kitu, zásahy do jiných repozitářů, změna Záměru.
Platí vždy: jádro kitu přečte člověk za 5 minut. Vedle MASTER.md, specs/ a gitu nevzniká žádný další zdroj pravdy. Názvy souborů, složek a nástrojů jsou anglicky.

## Rozhodnuto
<!-- datum · co · kdo (člověk (doporučeno) | člověk (jinak) | agent). Posledních ~10, starší v gitu. -->

- 2026-09-23 · nástroj přejmenován z Velín na Master (MASTER.md, master/), názvy anglicky · člověk (jinak)
- 2026-09-23 · Master jen přidán (docs/, master/, MASTER.md); stávající soubory beze změny · agent
- 2026-09-23 · texty Masteru česky; překlad jen při zveřejnění · agent
- 2026-09-23 · backbone.md a similar-work.md z předchozího sezení nechány beze změny a necommitnuté · agent
