#!/usr/bin/env python3

class Section(object):
    def __init__(self,elf,id):
        self.elf = elf
        self.id = id
    
    def get_id(self):
        return self.id

class WorkArea(object):
    def __init__(self,instruction):
        self.elf_one_section_list = []
        self.elf_two_section_list = []
        self.elf_one = instruction.split(",")[0]
        self.elf_two = instruction.split(",")[1]
        start = int(self.elf_one.split("-")[0])
        stop = int(self.elf_one.split("-")[1])
        for area in range(start,stop + 1):
            self.elf_one_section_list.append(Section("1",area))
        start = int(self.elf_two.split("-")[0])
        stop = int(self.elf_two.split("-")[1])
        for area in range(start, stop + 1):
            self.elf_two_section_list.append(Section("2",area))
    
    def is_duplication(self):
        duplicate = False
        elf_one_sections = []
        elf_two_sections = []
        for section in self.elf_one_section_list:
            elf_one_sections.append(section.get_id())
        
        for section in self.elf_two_section_list:
            elf_two_sections.append(section.get_id())

        if(all(x in elf_one_sections for x in elf_two_sections)):
            duplicate = True
        if(all(x in elf_two_sections for x in elf_one_sections)):
            duplicate = True

        if duplicate:
            return True
    def is_overlap(self):
        overlap = False
        elf_one_sections = []
        elf_two_sections = []
        for section in self.elf_one_section_list:
            elf_one_sections.append(section.get_id())
        
        for section in self.elf_two_section_list:
            elf_two_sections.append(section.get_id())

        if(any(x in elf_one_sections for x in elf_two_sections)):
            overlap = True
        if(any(x in elf_two_sections for x in elf_one_sections)):
            overlap = True

        if overlap:
            return True

work_area_list = []
work_area_count = 0
work_area_duplicates = 0
work_area_overlap = 0

with open("input.txt") as file:
    for line in file:
        work_area_list.append(WorkArea(line))
        work_area_count = work_area_count + 1

print(f"{work_area_count} work areas processed")

for area in work_area_list:
    if area.is_duplication():
        work_area_duplicates = work_area_duplicates + 1
    if area.is_overlap():
        work_area_overlap = work_area_overlap + 1

print(f"{work_area_duplicates} work areas are duplicates")

print(f"{work_area_overlap} work areas are overlaps")
