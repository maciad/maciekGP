from random import Random
from ProgramRunContext import ProgramRunContext
import math
import operator
from copy import deepcopy
from ProgramGenerator.TreeGenerator import *
from evolution.Crossover import Crossover


class Evolution:
    random = Random()

    @staticmethod
    def perform_evolution(test_set, max_generations=150, population_size=1000, program_size=15):

        print("STARTING EVOLUTION FOR TEST SET:" + test_set.name)

        current_generation_index = 1

        # create initial population
        population = []
        for i in range(population_size):
            population.append(generate_program_node_count(program_size))  # TODO: change to config

        while current_generation_index < max_generations:
            evaluated_population = Evolution.evaluate_population(population, test_set, test_set.grading_function, test_set.config.max_execution_time)
            best_program, best_fitness = min(evaluated_population.items(), key=operator.itemgetter(1))
            avg_fitness = sum(evaluated_population.values()) / len(evaluated_population)
            avg_size = sum([len(program.nodes) for program in population]) / len(population)
            print("================================================================================================================================================================================================")
            print("GENERATION: " + str(current_generation_index) + "\nBEST FITNESS: " + str(best_fitness), "\nAVG FITNESS: " + str(avg_fitness), "\nAVG SIZE: " + str(avg_size) + '\n')
            print(best_program)
            if best_fitness <= test_set.threshold:
                break

            new_population = []
            # add 5% of the best programs to the new population
            best_programs = sorted(evaluated_population, key=evaluated_population.get)
            for i in range(int(population_size * 0.05)):
                new_population.append(best_programs[i])

            while len(new_population) < population_size:
                # mutation
                if Evolution.random.random() < test_set.config.mutation_chance:
                    program = Evolution.random.choice(population)
                    while not program.can_be_mutated():
                        program = Evolution.random.choice(population)
                    new_program = deepcopy(program)
                    type_to_mutate = type(Evolution.random.choice(new_program.mutables))
                    while not new_program.has_node_of_type(type_to_mutate):
                        type_to_mutate = type(Evolution.random.choice(new_program.mutables))
                    new_program.mutate(type_to_mutate)
                    new_population.append(new_program)
                # crossover
                else:
                    success = False
                    while not success:
                        parent1 = Evolution.tournament_selection(evaluated_population)
                        parent2 = Evolution.tournament_selection(evaluated_population)
                        if parent1 != parent2:
                            new_program_1, new_program_2 = Crossover.cross_programs(parent1, parent2, test_set.config)
                            if new_program_1 is not None and new_program_2 is not None:
                                new_population.append(new_program_1)
                                new_population.append(new_program_2)
                                success = True

            population = new_population
            current_generation_index += 1

        return best_program

    @staticmethod
    def tournament_selection(evaluated_population, tournament_size=5):
        target = Evolution.random.choice(list(evaluated_population.keys()))
        for i in range(tournament_size - 1):
            competitor = Evolution.random.choice(list(evaluated_population.keys()))
            while evaluated_population[competitor] == math.inf:
                competitor = Evolution.random.choice(list(evaluated_population.keys()))
            if target is None or evaluated_population[competitor] < evaluated_population[target]:
                target = competitor
        return target

    @staticmethod
    def evaluate_population(population, test_set, grading_function, max_actions):
        result = {}
        for program in population:
            grades = []
            for test_case in test_set.test_cases:
                program_run_context = ProgramRunContext()
                program_run_context.input = test_case.input.copy()
                program_run_context.max_executed_actions = max_actions
                program.invoke(program_run_context)
                if not program_run_context.has_timed_out():
                    grades.append(grading_function(test_case, program_run_context))
                else:
                    grades.append(math.inf)
                    break
                result[program] = sum(grades) / len(grades)  # TODO: zastanowic sie czy to jest poprawne
        return result

