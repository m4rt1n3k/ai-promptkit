# Review ai-promptkit

Hodnocený stav: commit `07b79f4` (8. 9. 2026) a necommitnuté `docs/backbone.md` a `docs/similar-work.md` z 23. 9. Měřítkem je účel popsaný v [purpose.md](purpose.md).

## Verdikt

Repo svůj účel zatím neplní. Principy jsou dobré, některé výborné: pravomoc člověka nad nevratnými kroky, kázeň v důkazech, jedna nejistota na otočku a zásada, že se nejdřív postaví provozní řetězec a začnou se sbírat data. Jako nástroj ale kit nefunguje, a to z pěti důvodů:

1. Současnou verzi nepoužívá žádný projekt.
2. Člověku práci přidává. Vybírá role, přenáší výstupy mezi nástroji a drží stav v hlavě.
3. Kontinuitu mezi sezeními, kvůli které kit vznikl, záměrně vypustil.
4. Hierarchii agentů popisuje, ale nemá pro ni mechanismus.
5. Nedá se ověřit, jestli pomáhá. Pravidla jsou psaná próza, kterou nic nekontroluje ani neměří.

Návrh v `backbone.md` jde správným směrem, protože zjednodušuje. Architekturu ale ponechává: vstup píše člověk, páteří je Spec Kit a stav mezi otočkami nese člověk.

## Co repo dnes je

- 28 souborů a zhruba 12 000 slov anglické politiky, s dvěma novými poznámkami 13 600. Přečíst to celé trvá asi hodinu. Spustitelná je jen předvolba (preset) Spec Kitu, která přidává pole do tří šablon.
- Postup jedné otočky: člověk posoudí zralost a vybere roli (Engineer, Scientist nebo Business). Roli vyvolá dlouhým příkazem, první část její předávky vloží do `speckit.specify` a druhou do `speckit.plan`. Pak projde brány, výsledek nasadí a pozorování z provozu ručně přenese do další otočky.
- Kolem otočky je kaskáda: nápad, návrh projektu (Projectant pro UCEEB a TAČR), vývoj v DEV|L, článek a přenos do praxe.
- `backbone.md` tohle zužuje na jednu kartu s osmi poli, kterou píše člověk, a na jeden běh `specify workflow run speckit`.

## Co ukazuje skutečné použití

O nástroji nejvíc řekne, jak se používá. Prošel jsem repozitáře v `CODE/team-me`:

- Kit se připíná jako submodul `extern/ai-promptkit` jen ve dvou repozitářích: `asset-ontology` ho má na `4201e8f` (23. 6.), `asset-classes` na `91afb72` (16. 7.). Verzi s DEV|L, rolemi a Spec Kitem (od 3. 9.) nepoužívá žádný projekt. Ostatní aktivní repa, například `asset-runtime` a `emo-cez`, kit nemají vůbec.
- V projektech se skutečně udržují čtyři věci. `docs/devlog.md` se zápisy od člověka a agentů (Codex, Cursor Agent, Composer, Grok). Projektový `prompts/handoff.md` s oddílem „Domain invariants to preserve“ (kW a W, znaménka toků, `PVarray` jen pod `PVinverter`). Osm ADR v `asset-ontology`. A `TODO.md`, jehož aktivní stopa bývá prázdná. Právě tyto věci zářijová přestavba z kitu odstranila: ADR-0001 je nahrazené a konvence zakazují handoff i devlog.
- V `team-me/.specify` je od 1. 9. inicializovaný Spec Kit 1.0.2 s integrací pro Cursor a workflow `speckit`. Ústava je nevyplněná šablona a `specs/` neexistuje. Preset kitu vyžaduje `speckit >= 1.0.4`, takže v této instalaci bez upgradu ani nejde nainstalovat.
- Instrukce Spec Kitu pro agenta mají v `team-me/.cursor/skills` dohromady asi 130 kB, samotný `speckit-checklist` 22 kB. K tomu kit přidává svých 12 000 slov.
- Od 2. 6. do 23. 9. prošel kit šesti zásadními přestavbami: kity příkazů, knihovna promptů, minimální submodul, DEV|L se Spec Kitem, kaskáda s Projectantem a skills, nakonec backbone. Žádná z nich nevycházela z problémů naměřených v projektu a projekty se na nové verze nepřevedly.

## Podobné přístupy

### Vývoj řízený specifikací (Spec Kit, Kiro, Tessl, OpenSpec, BMAD)

Specifikace, plán a úkoly vzniknou před kódem a člověk je schvaluje. Kritici se shodují:

- Böckeler ([martinfowler.com](https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)) popisuje velké množství opakujícího se markdownu k revizi a zbytečně těžký postup pro malé změny. Píše, že by raději revidovala kód.
- [Marmelab](https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html) mluví o „Markdown Madness“ a o dvojí revizi, specifikace i kódu. Ve velkých existujících kódových bázích je podle nich postup skoro nepoužitelný.
- [Sibylline](https://sibylline.dev/articles/2026-01-28-problems-with-spec-driven-development/) popisuje, že agenti berou specifikaci jako návrh a splní z ní 80–90 %.

Z toho plyne:

- **Vzít:** specifikaci jen pro větší a rizikovější změny; rozšíření šablon přes preset `append`.
- **Vyhnout se:** Spec Kitu jako páteři všeho a člověku jako revizorovi dlouhých dokumentů. Projekty uživatele jsou existující kódové báze, kde je tato slabina nejvýraznější.

### Harness pro dlouhé běhy a paměť agenta

- **Anthropic, [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents):** první sezení připraví prostředí, soubor s průběhem a seznam funkcí s polem `passes`. Každé další sezení přečte průběh, seznam funkcí a git log, udělá jednu věc, ověří ji a commitne. Pole `passes` se smí přepnout až po ověření.
- **Ralph loop ([Huntley](https://ghuntley.com/ralph/)):** stejný prompt ve smyčce, každá iterace s čerstvým kontextem. Stav nese plán na disku a git. Kvalitu drží testy, které musí projít, než agent smí commitnout.
- **[Beads](https://github.com/steveyegge/beads) (Yegge):** graf úkolů v gitu jako externí paměť agenta. `bd ready` vrátí, co je odblokované. Do `AGENTS.md` stačí jeden řádek.
- **HumanLayer, [Advanced Context Engineering](https://www.humanlayer.com/blog/advanced-context-engineering):** výzkum, plán, implementace a průběžná komprese kontextu. Člověk reviduje výzkum a plán, protože tam má chyba největší dopad: chybná věta ve výzkumu může vést k tisícům chybných řádků kódu.

Z toho plyne:

- **Vzít:** malý strukturovaný stav na disku a git jako paměť; stav, který se smí změnit jen po ověření; automatické kontroly jako podmínku postupu; jeden řádek v `AGENTS.md` místo vyvolávacích příkazů.
- **Vyhnout se:** stovkám úkolů jako rozhraní pro člověka. Úkoly jsou rozhraní pro agenty.

### Hierarchie a delegování

- **Anthropic, [multi-agent research](https://www.anthropic.com/engineering/multi-agent-research-system):** vedoucí agent rozdělí práci mezi paralelní pracovníky s vlastním kontextem. Každé zadání musí mít cíl, tvar výstupu, vodítko k nástrojům a jasné hranice. Bez toho pracovníci zdvojují práci a nechávají mezery.
- **Cognition, [Don't Build Multi-Agents](https://cognition.com/blog/dont-build-multi-agents) (2025) a [Multi-Agents: What's Actually Working](https://cognition.com/blog/multi-agents-working) (2026):** paralelní agenti, kteří každý zvlášť zapisují, dělají neslučitelná skrytá rozhodnutí. Dnes fungují systémy, kde zapisuje jeden agent a ostatní dodávají úsudek, ne změny. Recenzent s čistým kontextem najde chyby, které autor nevidí.
- **Claude Code:** subagenty lze vnořovat až do tří úrovní. Experimentální agent teams mají vedoucího a sdílený seznam úkolů. Subagenty má i Cursor.
- **Gas Town (Yegge):** trvalé role a efemérní pracovníci nad Beads. Silné, ale složité.
- **Google DeepMind, [Intelligent AI Delegation](https://arxiv.org/abs/2602.11865) (2026):** delegování chápe jako přenos pravomoci a odpovědnosti s jasným záměrem, hranicemi a mechanismem důvěry. Upozorňuje na „authority gradient“: kde je velký rozdíl v postavení, podřízený mlčí a chyby projdou.

Z toho plyne:

- **Vzít:** jednoho vedoucího agenta, který jediný zapisuje sdílený stav; pracovníky s ohraničeným zadáním, kteří vracejí zprávu; ověřovatele s čistým kontextem; stejný tvar zadání a zprávy na každé úrovni.
- **Vyhnout se:** personám, které vyvolává člověk, a více zapisovatelům sdíleného stavu.

### Rozhraní mezi člověkem a agentem

- **LangChain [Agent Inbox](https://github.com/langchain-ai/agent-inbox):** agent se zastaví a pošle do fronty žádost. Člověk ji přijme, upraví, odpoví na ni, nebo ji ignoruje.
- **Karpathy, [Software 3.0](https://www.latent.space/p/s3):** agent generuje a člověk ověřuje, takže cyklus mezi nimi musí být rychlý. Autonomii nastavuje člověk jako posuvník podle úkolu.

Z toho plyne:

- **Vzít:** člověk dostává frontu rozhodnutí, ne proud textu; autonomie je nastavitelná.

### AI ve vědě

- **Google [AI co-scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/):** oddělení agenti generují hypotézy, kritizují je, pořádají mezi nimi turnaj a vylepšují je. Vědec zadává cíl a hodnotí výsledek.
- **AlphaEvolve (Google DeepMind):** hledání algoritmů pohání automatický hodnotitel. Kde takový hodnotitel existuje, může agent iterovat sám.
- **Licklider, Man-Computer Symbiosis (1960)** tuto dělbu popsal přesně: člověk stanoví cíle, formuluje hypotézy, určí kritéria a hodnotí. Stroj dělá rutinní práci, která rozhodnutí připraví.

Z toho plyne:

- **Vzít:** kdo tvrzení vytvoří, ten ho neověřuje. Automatický hodnotitel je páka pro autonomii. Pro projekty uživatele to znamená, že data sbíraná od prvního provozního řetězce jsou budoucí hodnotitel vědecké práce.

### Lidský faktor a řízení provozu

- **Supervisory control (Sheridan):** operátor plánuje, učí automatiku, sleduje ji, zasahuje a učí se. Ruční řízení nahrazuje dohled.
- **Ironie automatizace (Bainbridge, 1983):** člověk jako pasivní dozor je špatný dozor. Potřebuje smysluplná rozhodnutí, ne jen potvrzování.
- **Alarm management (EEMUA 191, ISA-18.2, [přehled metrik](https://isa.ie/wp-content/uploads/2016/06/Alarm_System_Performance_Metrics_Kim_Van_camp.pdf)):** v ustáleném provozu nejvýš 1–2 alarmy za 10 minut. Každý alarm musí vyžadovat zásah a vést k doporučené reakci. Obtěžující alarmy se odstraňují.
- **Mission command ([ADP 6-0](https://irp.fas.org/doddir/army/adp6_0.pdf)):** velitel předá záměr (účel, konečný stav, meze) a podřízený v jeho rámci rozhoduje sám. Záměr zná dvě úrovně nad sebou a svůj plán ohlásí zpět (backbrief).
- **Vaccaro, Almaatouq, Malone ([Nature Human Behaviour, 2024](https://www.nature.com/articles/s41562-024-02024-1)):** metaanalýza 106 experimentů. Dvojice člověk a AI je v průměru horší než lepší z obou samotných. Ztrácí u rozhodovacích úloh a získává u tvorby. Zisk nastává tam, kde je člověk sám lepší než AI.
- **METR ([2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), [2026](https://metr.org/blog/2026-02-24-uplift-update/)):** zkušení vývojáři byli s AI o 19 % pomalejší a přitom věřili, že jsou o 20 % rychlejší. Novější data naznačují spíš zrychlení, ale s velkou nejistotou. Pocit zrychlení tedy není důkaz zrychlení.

Z toho plyne:

- **Vzít:** člověk rozhoduje jen tam, kde něco přidává; počet výzev pro něj je rozpočet; každá výzva nese doporučení; přínos se měří, ne odhaduje.

### Rámce výzkumného cyklu

Hevnerův design science (relevance, rigor, design), living lab a action design research mají stejný cyklus jako DEV|L: problém z provozu, artefakt, zásah v provozu a učení z něj. Stage-Gate dává branám čtyři výsledky: pokračovat, zastavit, odložit, přepracovat. TRL a příbuzné stupnice jsou diagnostika pro poskytovatele.

- **Vzít:** cyklus s návratem do provozu; brány jako rozhodnutí se čtyřmi výsledky.
- **Vyhnout se:** lineární stupnici jako motoru práce.

### Co mají úspěšné přístupy společné

1. Stav žije na disku, je malý a strukturovaný a git je jeho deník.
2. Jeden vedoucí agent zapisuje, pracovníci s izolovaným kontextem dodávají úsudek.
3. Automatické ověřování je podmínkou postupu.
4. Člověk stojí na místech s největší pákou a počet výzev pro něj je omezený.
5. Autonomie je posuvník, který člověk nastavuje.

ai-promptkit z toho má jen část čtvrtého bodu, brány. Ty ale stojí na dlouhých dokumentech, ne na rozhodnutích.

## Slabá místa

Seřazeno podle dopadu. U každého je důkaz a důsledek.

### 1. Kit se nepoužívá

**Důkaz:** oddíl [Co ukazuje skutečné použití](#co-ukazuje-skutečné-použití).

**Důsledek:** nástroj, který se nepoužívá, účel neplní a nedostává zpětnou vazbu. Každá další přestavba pak vychází jen z úvah.

### 2. Člověk je směrovač, písař i paměť

**Důkaz:** `agents/README.md` obsahuje 14 různých vyvolávacích příkazů `Read extern/ai-promptkit/...`. Předávka o dvou částech existuje jen v chatu a člověk ji ručně vkládá do `speckit.specify` a `speckit.plan`. V `backbone.md` člověk každou otočku píše kartu s osmi poli a výsledky z provozu přenáší do další karty.

**Důsledek:** nejdražší zdroj, pozornost člověka, se spotřebovává na práci, kterou agent zvládne lépe. Psát strukturovaný vstup znamená vybavovat si z paměti, a to je pro člověka těžší než vybrat z nabídnutých možností.

### 3. Kontinuita byla vypuštěna

**Důkaz:** ADR-0001 je nahrazené. `devl-workflow.md` píše „This kit intentionally provides no separate handoff“ a `conventions.md` zakazuje handoff, devlog i souhrny sezení. Jediný trvalý kontext je Spec Kit a ten pokrývá jen jednu softwarovou feature.

**Důsledek:** doménové invarianty, rozhodnutí napříč featurami, otevřené otázky a stav nápadu nebo návrhu projektu nemají kde žít a zůstávají v chatu. Projekty přitom ukazují, že je kontinuita potřeba (handoff s invarianty, devlog), a všechny úspěšné harnessy ji řeší malým stavem na disku. Obava ze dvou zdrojů pravdy byla oprávněná. Řešením ale měl být jeden malý stav, ne žádný.

### 4. Hierarchie agentů je jen na papíře

**Důkaz:** role jsou texty, které vyvolává člověk („A role is a responsibility, not a requirement to spawn a separate process“). Kit nemá protokol pro vedoucího agenta, jednotný tvar zadání a zprávy mezi úrovněmi ani ověření tvrzení jiným agentem. Sdílená předávka popisuje jediný krok, ke Spec Kitu.

**Důsledek:** Cursor i Claude Code subagenty nativně mají, a přesto zůstává nevyužitá paralelní práce i oddělení autora od kritika.

### 5. Člověk rozhoduje abstraktně, ne konkrétně

**Důkaz:** každá otočka začíná „human maturity judgment and agent selection“. K takovému rozhodnutí potřebuje člověk v hlavě celý model kitu. Kit přitom nemá tvar pro otázky na člověka, limit jejich počtu ani postup pro případ, že člověk neodpoví.

**Důsledek:** člověk rozhoduje věci, ve kterých nic nepřidává (podle metaanalýzy Vaccaro a kol. tam dvojice člověk a AI ztrácí), a pro konkrétní rozhodnutí s doporučením a dopady nemá rozhraní.

### 6. Stupně zralosti jsou další abstrakce

**Důkaz:** stupně se na 19 řádcích pojmenovávají různě: Preliminary Mockup, Minimum Viable Solution, excellent core, working chain, market-ready ecosystem. ADR-0002 mluví o „excellent defensible core“, `devl-workflow.md` o „Minimum Viable Solution“. Stupně nejsou brány, a tak neřídí nic, co by neřídil samotný důkaz.

**Důsledek:** člověk kromě důkazů posuzuje i stupeň. Zralost je přitom jen pohled na stav tvrzení: řetězec na reálné budově je změřený, metoda je porovnaná se základní úrovní, přijetí se zopakovalo v dalším prostředí.

### 7. Politika v próze, zdvojená a rozjetá

**Důkaz:** kaskádu zmiňuje nebo převypráví 16 z 28 souborů a zákaz vymýšlení se opakuje ve čtyřech. Kopie se už rozešly: ADR-0002 říká, že role vrací jen prompt pro `speckit.specify`, zatímco `agents/README.md` popisuje předávku o dvou částech. Na straně agenta se sčítají instrukce kitu a asi 130 kB instrukcí Spec Kitu.

**Důsledek:** benchmark [IFScale](https://arxiv.org/abs/2507.11538) z roku 2025 ukázal, že modely se hustotou instrukcí zhoršují. [Novější replikace](https://github.com/Arize-ai/instruction-budget/blob/main/IFSCALE_REPLICATION.md) ale naznačuje, že nejsilnější modely roku 2026 ji snášejí mnohem lépe. Silnější je proto argument z lidské strany: 12 000 slov nikdo neudrží konzistentních a nikdo je při práci nečte.

### 8. Chybí zpětná vazba

**Důkaz:** `doctor.md` kontroluje instalaci, piny a nadpisy ve specifikaci. Nepozná hypotézu povýšenou na požadavek, vymyšleného partnera ani tři „dominantní“ nejistoty. Neexistují testovací scénáře, metriky ani pilot.

**Důsledek:** nedá se zjistit, jestli kit pomáhá, a podle METR se pocitu zrychlení věřit nedá. Šest přestaveb za necelé čtyři měsíce bez dat je toho příznakem.

### 9. Křehká vazba na Spec Kit

**Důkaz:** Spec Kit vydal za měsíc verze 1.0.0 až 1.0.9 a preset chce ≥ 1.0.4, zatímco v `team-me` je 1.0.2. Vestavěné workflow `speckit`, na kterém stojí `backbone.md`, posílá stejný text `{{ inputs.spec }}` jako argument všem čtyřem příkazům (specify, plan, tasks, implement). Odvození a podklady pro plán tak nemají vlastní kanál. Brány workflow jsou navíc v CLI (`specify workflow resume`), mimo chat, ve kterém člověk pracuje.

**Důsledek:** dokumentace kitu o schopnostech Spec Kitu rychle stárne. Obřad je stejný pro malou opravu i velkou změnu, a právě na to upozorňuje kritika vývoje řízeného specifikací.

### 10. Rozsah, který nástroj neumí

**Důkaz:** `projectant.md` předpokládá napojení na Teams, interní aplikace UCEEB a systémy TAČR a mnoho řádků věnuje tomu, co role nesmí tvrdit, když napojení chybí. Skutečná práce pro TAČR (vyplnění dotazníku z podkladu ve Wordu, v jiném sezení) proběhla mimo kit, přes prohlížeč.

**Důsledek:** kit popisuje ideální instituci místo nástrojů, které agent má. Text roste a důvěryhodnost klesá.

### 11. Kit počítá s jedním repem, práce je ekosystém

**Důkaz:** `asset-ontology`, `asset-classes`, `asset-runtime` a konektor sdílejí kontrakty a vlastnictví popsané v `asset-classes/docs/ecosystem-plan.md`. Kit nemá místo pro společný záměr a rozhodnutí napříč repy a dva spotřebitelé připínají dvě různé verze kitu.

**Důsledek:** rozhodnutí o hranicích mezi repy žijí roztroušená po jednotlivých repech nebo v chatu.

### Zvlášť k `backbone.md`

Je to dosud nejlepší krok: zužuje vstup na jeden, ruší volbu role před každou otočkou a drží pravidlo jedné nejistoty. Slabiny:

- Kartu s osmi poli píše člověk, takže nejtěžší kognitivní práce zůstává na něm. Důvodem je omezení nástroje: krok workflow nepředá výstup promptu dalšímu kroku. Z omezení nástroje se tak stala práce pro člověka.
- Týká se jen softwaru. Nápad, návrh projektu, článek a zpráva pro TAČR, tedy velká část skutečné práce, vypadávají.
- Stav mezi otočkami nese člověk: do nové karty ručně přepisuje, co se v provozu stalo.
- Závisí na `specify workflow` v konkrétní verzi a na branách v CLI mimo chat.
- Hierarchii agentů neřeší.

## Co je dobré a má zůstat

- Pravomoc člověka nad nevratnými kroky a kroky navenek.
- Kázeň v důkazech: rozlišovat fakt, měření, předpoklad a hypotézu, uvádět zdroj a datum, nemazat negativní výsledky, označovat simulaci.
- Jedna dominantní nejistota na otočku. Otočka končí pozorováním v provozu.
- Nejdřív celý provozní řetězec od dat k výstupu na budově a sběr dat od prvního dne. Tak vzniká budoucí hodnotitel vědecké práce. Je to nejcennější myšlenka kitu.
- Skills `field-chain` a `scientific-optimization`. Obsahově jsou výborné a slouží jako rozhodovací kritéria, ne jako šablony zpráv.
- Odkazovat místo kopírovat. Připnutá verze kitu v submodulu.

## Co z toho plyne pro nástroj

- Člověk dodává jen záměr, rozhodnutí a pozorování z reality.
- Sdílený stav je jeden: malý, na disku a čitelný pro člověka i agenta. Git je jeho deník.
- Jeden vedoucí agent a pracovníci se stejným tvarem zadání a zprávy na každé úrovni. Kdo tvrzení vytvořil, ten ho neověřuje.
- Otázky pro člověka tvoří frontu s limitem. Každá má možnosti, doporučení a postup pro případ, že člověk neodpoví.
- Zralost se čte ze stavu tvrzení, bez samostatné stupnice.
- Pravidla vynucuje kontrola, ne další próza.
- Úspěch se měří na pilotu s předem daným prahem.

Takový nástroj navrhuje [master.md](master.md).

## Další zdroje

- Licklider, J. C. R. *Man-Computer Symbiosis.* IRE Transactions on Human Factors in Electronics, 1960.
- Sheridan, T. B. *Telerobotics, Automation, and Human Supervisory Control.* MIT Press, 1992.
- Bainbridge, L. *Ironies of Automation.* Automatica 19(6), 1983.
- Hevner, A. *A Three Cycle View of Design Science Research.* Scandinavian Journal of Information Systems, 2007.
- EEMUA 191, *Alarm systems: a guide to design, management and procurement*; ANSI/ISA-18.2, *Management of Alarm Systems for the Process Industries*.
- Cooper, R. G. *Stage-Gate Systems: A New Tool for Managing New Products.* Business Horizons, 1990.
- Spec Kit, [releases](https://github.com/github/spec-kit/releases); Claude Code, [sub-agents](https://code.claude.com/docs/en/sub-agents) a [agent teams](https://code.claude.com/docs/en/agent-teams).
