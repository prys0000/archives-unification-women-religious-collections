# AUTHORITY FILE PACKAGE - README
## Complete Name Control System for Archival Collections

---

### Complete Authority Control System

This package offers guidance for creating and maintaining a professional authority file for names found in HARC archival collections. It is based on national and international archival standards and addresses issues related to name consistency and disambiguation. The document provides a workflow to help resolve these issues and standardize the collections.

---

## PROBLEM 

### Before Authority Control

**Researcher searches for "Sister Mary Catherine":**
- Finds 15 different people, all called "Sister Mary Catherine"
- Can't tell which is which
- Misses relevant materials filed under variant names
- No biographical context

**Archivist processing materials:**
- Encounters "Sr. M. Catherine Smith" in one box
- Finds "Mary Catherine Smith, OSF" in another box  
- Sees "Sister Mary Catherine" in a third box
- Are these the same person? No way to know.

### Authority Control (v1)

**Researcher searches for "Sister Mary Catherine":**
- Authority file shows all distinct "Sister Mary Catherines"
- Each has unique authorized name: Smith, Mary Catherine, OSF
- All variant names link to authorized form
- Biographical notes provide context
- Related materials easily identified

**Archivist processing materials:**
- Checks authority file
- Finds existing record: Smith, Mary Catherine, OSF [PERS-042]
- Uses authorized form consistently
- Adds any new name variants discovered
- Links materials to authority record

---

## FILES

### 1. **Authority_File_Persons_Agents.xlsx** 
**The Main Database**

**Contains 3 worksheets:**

**Sheet 1: Authority Records**
- Main data entry form
- Example records showing proper formatting
- Fields for all biographical and administrative data
- Color-coded with instructions

**Sheet 2: Naming Guidelines**  
- Formatting rules
- Guide for potential scenarios
- Based on LCNAF, RDA, ISAAR(CPF) standards
- Examples and guidelines

**Sheet 3: Quick Reference**
- One-page summary of essential rules
- Common mistakes and corrections
- Quick lookup tables
- Daily use reference

**[View Authority File](computer:///mnt/user-data/outputs/Authority_File_Persons_Agents.xlsx)**

---

### 2. **Authority_File_Documentation.md**
**Complete Implementation Guide**

**Pages covering:**
- What authority control is and why it matters
- The "Sister Mary Catherine problem" explained
- Authorized name format breakdown
- Field-by-field instructions
- Date formatting standards
- Biographical note guidelines
- Data quality levels
- Source documentation
- Complete workflow from start to finish
- Common challenges and solutions
- Integration with finding aids
- Training materials
- Professional standards reference
- FAQ section

**[View Documentation](computer:///mnt/user-data/outputs/Authority_File_Documentation.md)**

---

### 3. **Name_Extraction_Worksheet.xlsx**
**Practical Collection Tool**

**Purpose:** Capture names as you process collections

**Features:**
- Simple data entry form
- Fields for source location tracking
- Priority assessment
- Status tracking
- Batch processing support
- Instructions included

**Use this to:**
- Record names as you encounter them
- Track where names were found
- Prioritize which need authority records first
- Batch process similar names together

**[View Extraction Worksheet](computer:///mnt/user-data/outputs/Name_Extraction_Worksheet.xlsx)**

---

## GETTING STARTED

### Quick Start (30 minutes)

1. **Read this README** (5 min)
2. **Open Authority_File_Persons_Agents.xlsx** (10 min)
   - Review Sheet 3: Quick Reference
   - Look at example records in Sheet 1
3. **Skim Authority_File_Documentation.md** (15 min)
   - Read "Understanding the Authorized Name Format"
   - Review "The Sister Mary Catherine Problem"

### Full Implementation (2-3 hours)

1. **Study the Documentation** (60 min)
   - Read Authority_File_Documentation.md completely
   - Review all sections of the Excel file
2. **Practice with Examples** (30 min)
   - Format 5-10 names from your collections
   - Create sample authority records
3. **Set Up Your Workflow** (30 min)
   - Decide on ID numbering scheme
   - Identify priority names to enter
   - Plan source material gathering
4. **Begin Data Entry** (ongoing)

---

## THE AUTHORIZED NAME FORMAT

### For Religious Sisters/Brothers

**Standard Format:**
```
Surname, Given Name [Religious Name], Post-Nominals
```

**Examples:**
```
✓ Smith, Mary Catherine, OSF
✓ O'Brien, Margaret Mary, BVM  
✓ García, María Teresa, SSND
```

**Why this format?**
- Surname first = standard for alphabetizing
- Religious name = name used in religious life
- Post-nominals = identifies congregation
- **Result: Each sister has unique, findable name**

### For Organizations/Institutions

**Standard Format:**
```
Institution Name (City, State Abbreviation)
```

**Examples:**
```
✓ St. Mary's Academy (Chicago, Ill.)
✓ Mundelein College (Chicago, Ill.)
✓ Mount Carmel Motherhouse (Dubuque, Iowa)
```

---

## KEY CONCEPTS

### 1. Authorized Name
**One official form** used consistently everywhere

### 2. Variant Names  
**All other forms** linked to authorized name

### 3. Authority ID
**Unique identifier** (PERS-001, CORP-001)

### 4. Disambiguation
**Making distinctions** between people with similar names

### 5. Data Quality
**Reliability level:** Verified | Preliminary | Needs Review

---

## ESSENTIAL FIELDS

### Minimum Required (7 fields)

1. **Authority_ID** - Unique number
2. **Authorized_Name** - Official form
3. **Name_Type** - Person or Corporate Body
4. **Congregation** - Religious order
5. **Status** - Active/Deceased/Departed
6. **Created_Date** - When record made
7. **Data_Quality** - Reliability level

### Highly Recommended (6 more fields)

8. **Birth_Name** - Legal birth name
9. **Religious_Name** - Name in religious life
10. **Birth_Date** - When born
11. **Death_Date** - When died
12. **Variant_Names** - All other name forms
13. **Authority_Source** - Where info from

### Complete Record (27 total fields)

All fields documented in the Excel file and documentation

---

## SOLVING THE DUPLICATE NAME PROBLEM

### The Challenge

Many religious sisters shared the same religious name:
- Sister Mary Catherine (appears 15 times in your collections)
- Sister Mary Margaret (appears 12 times)
- Sister Mary Joseph (appears 20 times)

### The Solution

**Use birth surname to distinguish:**

```
Different people, now clearly distinguished:

Smith, Mary Catherine, OSF [PERS-001]
Jones, Mary Catherine, OSF [PERS-045]  
O'Brien, Mary Catherine, BVM [PERS-127]
Murphy, Mary Catherine, BVM [PERS-203]
```

**Each is unique and findable!**

---

## TYPICAL WORKFLOW

### Step 1: Encounter a Name
While processing collection, you see: "Sister Mary Catherine Smith"

### Step 2: Check Authority File
Search: Is there already a record?

### Step 3A: If Record Exists
- Use authorized form: Smith, Mary Catherine, OSF
- Add any new variants you found
- Note any new biographical details

### Step 3B: If New Name
- Record in Name Extraction Worksheet
- OR create authority record immediately (if high priority)

### Step 4: Use in Finding Aids
- Folder title: Smith, Mary Catherine, OSF [PERS-042]
- Cross-references for all variants
- Researchers can find via any form of name

---

## PRIORITY SYSTEM

### High Priority - Create Immediately
- Names appearing in 10+ folders/boxes
- Congregation founders and leaders
- Major institution names
- People with extensive biographical materials

### Medium Priority - Batch Process
- Names appearing 3-9 times
- Important but less frequent names
- Secondary leadership roles

### Low Priority - As Time Permits
- Names appearing 1-2 times
- Mentioned in passing
- Create on researcher request

---

## PROFESSIONAL STANDARDS

This authority file follows these standards:

### Library of Congress Name Authority File (LCNAF)
- Name formatting conventions
- Authorized vs. variant forms
- Bibliographic citation standards

### Resource Description and Access (RDA)
- Descriptive cataloging rules
- Name authority principles
- Relationship documentation

### ISAAR(CPF) - International Standard
- Archival authority records
- Context and relationships
- Historical information

### Encoded Archival Context (EAC-CPF)
- XML encoding standards
- Machine-readable formats
- System interoperability

---

## INTEGRATION OPTIONS

### With Your Current System

**ArchivesSpace:**
- Import as agent records
- Link to archival objects
- Export as EAC-CPF

**CONTENTdm:**
- Use as controlled vocabulary
- Auto-complete in metadata
- Subject heading authority

**PastPerfect:**
- Import to Name Authority
- Link catalog records
- Search by authority ID

**Excel/Access:**
- Already in Excel format
- Easy to customize
- Import/export as CSV

**Custom Database:**
- Standard field structure
- CSV import ready
- SQL compatible

---

## CUSTOMIZATION

### What You Can Customize

✓ **Authority ID format** - Use your own numbering  
✓ **Field names** - Rename to match your system  
✓ **Additional fields** - Add congregation-specific data  
✓ **Biographical note format** - Adapt to your needs  
✓ **Data quality levels** - Define your own standards  

### What to Keep Standard

⚠️ **Authorized name format** - Keep for consistency  
⚠️ **Date format (ISO 8601)** - Industry standard  
⚠️ **Name type categories** - Standard classifications  
⚠️ **Post-nominals** - Official abbreviations  

---

## TRAINING RESOURCES

### For Project Managers
- Authority_File_Documentation.md (full read)
- Focus on: Why it matters, workflow, integration

### For Archivists/Processors
- Quick Reference sheet (print and keep handy)
- Authority_File_Documentation.md (reference)
- Name_Extraction_Worksheet.xlsx (daily use)

### For Volunteers/New Staff
- Quick Reference sheet only
- 1-hour training on basics
- Supervised practice with examples

### Training Time Estimates
- **Introduction:** 30 minutes
- **Detailed training:** 2-3 hours  
- **Hands-on practice:** 1-2 hours
- **Total:** Half day for thorough training

---

## LEARNING PATH

### Beginner (Week 1)
- [ ] Understand what authority control is
- [ ] Learn authorized name format
- [ ] Practice formatting 10 names
- [ ] Use Quick Reference sheet

### Intermediate (Week 2-4)
- [ ] Create 25-50 authority records
- [ ] Learn to handle duplicates
- [ ] Master variant name recording
- [ ] Document sources properly

### Advanced (Month 2-3)
- [ ] Handle complex cases independently
- [ ] Train others
- [ ] Customize for special needs
- [ ] Integrate with cataloging system

---

## COMMON QUESTIONS

**Q: How many names should I include?**
A: Start with frequently mentioned names. Add others as you process collections.

**Q: What if I can't find birth surname?**
A: Note as unknown, mark "Needs Review," continue research. See documentation for details.

**Q: Do I need to create records for everyone?**
A: Prioritize: Congregation members first, then major institutions, then others as relevant.

**Q: How long does this take?**
A: Simple record: 5-10 minutes. Complex research: 30-60 minutes. Batch processing is efficient.

**Q: Can I modify the fields?**
A: Yes, but keep core fields standard. Add custom fields as needed.

**Q: What about living members' privacy?**
A: Use factual, publicly available information. Avoid sensitive personal details.

---

## IMPLEMENTATION CHECKLIST

### Planning Phase
- [ ] Read all documentation
- [ ] Review example records
- [ ] Identify priority names (50-100 to start)
- [ ] Gather source materials
- [ ] Set up workspace

### Setup Phase
- [ ] Customize Authority ID format if needed
- [ ] Add any congregation-specific fields
- [ ] Print Quick Reference sheet
- [ ] Set up Name Extraction Worksheet
- [ ] Train staff/volunteers

### Implementation Phase
- [ ] Create first 25 authority records
- [ ] Review for consistency
- [ ] Refine workflow as needed
- [ ] Begin systematic processing
- [ ] Integrate with finding aids

### Maintenance Phase
- [ ] Schedule regular updates
- [ ] Review and upgrade preliminary records
- [ ] Add newly discovered information
- [ ] Respond to researcher queries
- [ ] Annual review and cleanup

---

## SUCCESS METRICS

### You'll know it's working when:

✓ Staff use authorized names consistently  
✓ Researchers can find materials easily  
✓ Duplicate name problems are solved  
✓ Biographical context enriches understanding  
✓ New staff can learn the system quickly  
✓ Finding aids are more useful  
✓ Cross-references work properly  

---

## RELATED DOCUMENTS

### Also in Your Package

From the archival organization project:
- Archival_Controlled_Series_Structure.xlsx
- Archival_Structure_Documentation.md
- Quick_Start_Guide.md
- Series_Crosswalk_Mapping.xlsx

Authority control integrates with these to create a complete archival system.

---

## SUPPORT RESOURCES

### Professional Organizations

**Society of American Archivists (SAA)**
- Authority control working groups
- Best practices guides

**Conference of Religious Archivists (CoRA)**
- Religious archive specialists
- Shared resources

**Program for Cooperative Cataloging (PCC)**
- NACO (Name Authority Cooperative)
- Training programs

### Online Resources

**Library of Congress Authorities**
- authorities.loc.gov
- Search existing authority records

**VIAF**
- viaf.org  
- International authority file

### Key Publications

- *Describing Archives: A Content Standard (DACS)*
- *RDA: Resource Description and Access*
- *ISAAR(CPF): International Standard*

---

## NEXT STEPS

### Today (30 minutes)
1. Open Authority_File_Persons_Agents.xlsx
2. Review Sheet 3: Quick Reference
3. Look at example records

### This Week (3-4 hours)
1. Read Authority_File_Documentation.md
2. Format 10 practice names
3. Create 5 sample authority records
4. Review and refine

### This Month (ongoing)
1. Identify 50-100 priority names
2. Begin systematic record creation
3. Train staff/volunteers
4. Integrate with processing workflow

### This Year
1. Build comprehensive authority file
2. Integrate with all finding aids
3. Establish maintenance routine
4. Evaluate and refine system

---

## FINAL NOTES

### Remember

✓ **Start small** - Begin with high-priority names  
✓ **Be consistent** - Use formats exactly as shown  
✓ **Document sources** - Future you will thank you  
✓ **Don't aim for perfection** - Better to have preliminary records than none  
✓ **Update regularly** - Authority files grow and improve over time  

### The Goal

Create a system where:
- Every name has one authorized form
- All variants lead to the authorized form
- Biographical context enriches understanding
- Researchers can find materials reliably
- Future archivists understand your decisions

---

## YOU'RE READY!

You now have a complete, professional authority control system ready for implementation. This system will:

✓ Solve the duplicate name problem  
✓ Make collections more discoverable  
✓ Provide valuable biographical context  
✓ Meet professional archival standards  
✓ Serve your congregation for generations  

**Start with the Quick Reference sheet and dive in. Good luck!** 

---

**Questions?** Review the comprehensive documentation file for detailed answers.

**Need help?** Consult the FAQ section or reach out to professional archival organizations.

**Ready to start?** Open the Authority File Excel sheet and begin with your first record!
