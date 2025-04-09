#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char id[101];
    int weight;
} Package;

typedef struct {
    int min_weight;
    int max_weight;
    int package_count;
    Package *packages;
} PostOffice;

typedef struct {
    char name[101];
    int post_office_count;
    PostOffice *post_offices;
} Town;

void print_all_packages(Town *town) {
    printf("%s:\n", town->name);
    for (int i = 0; i < town->post_office_count; i++) {
        printf("\t%d:\n", i);
        for (int j = 0; j < town->post_offices[i].package_count; j++) {
            printf("\t\t%s\n", town->post_offices[i].packages[j].id);
        }
    }
}

void transfer_packages(Town *source_town, int source_index, Town *target_town, int target_index) {
    PostOffice *source_office = &source_town->post_offices[source_index];
    PostOffice *target_office = &target_town->post_offices[target_index];

    Package *accepted_packages = malloc(sizeof(Package) * source_office->package_count);
    Package *rejected_packages = malloc(sizeof(Package) * source_office->package_count);

    int accepted_count = 0, rejected_count = 0;

    for (int i = 0; i < source_office->package_count; i++) {
        if (source_office->packages[i].weight >= target_office->min_weight &&
            source_office->packages[i].weight <= target_office->max_weight) {
            accepted_packages[accepted_count++] = source_office->packages[i];
        } else {
            rejected_packages[rejected_count++] = source_office->packages[i];
        }
    }

    source_office->packages = realloc(source_office->packages, sizeof(Package) * rejected_count);
    memcpy(source_office->packages, rejected_packages, sizeof(Package) * rejected_count);
    source_office->package_count = rejected_count;

    target_office->packages = realloc(target_office->packages, sizeof(Package) * (target_office->package_count + accepted_count));
    memcpy(target_office->packages + target_office->package_count, accepted_packages, sizeof(Package) * accepted_count);
    target_office->package_count += accepted_count;

    free(rejected_packages);
    free(accepted_packages);
}

Town *find_town_with_most_packages(Town *towns, int town_count) {
    int max_packages = -1;
    Town *result_town = NULL;

    for (int i = 0; i < town_count; i++) {
        int total_packages = 0;
        for (int j = 0; j < towns[i].post_office_count; j++) {
            total_packages += towns[i].post_offices[j].package_count;
        }
        if (total_packages > max_packages) {
            max_packages = total_packages;
            result_town = &towns[i];
        }
    }
    return result_town;
}

Town *find_town_by_name(Town *towns, int town_count, const char *name) {
    for (int i = 0; i < town_count; i++) {
        if (strcmp(towns[i].name, name) == 0) {
            return &towns[i];
        }
    }
    return NULL;
}

int main() {
    int town_count;
    scanf("%d", &town_count);

    Town *towns = malloc(sizeof(Town) * town_count);

    for (int i = 0; i < town_count; i++) {
        scanf("%s", towns[i].name);
        scanf("%d", &towns[i].post_office_count);
        towns[i].post_offices = malloc(sizeof(PostOffice) * towns[i].post_office_count);

        for (int j = 0; j < towns[i].post_office_count; j++) {
            int package_count, min_weight, max_weight;
            scanf("%d %d %d", &package_count, &min_weight, &max_weight);
            towns[i].post_offices[j].min_weight = min_weight;
            towns[i].post_offices[j].max_weight = max_weight;
            towns[i].post_offices[j].package_count = package_count;
            towns[i].post_offices[j].packages = malloc(sizeof(Package) * package_count);

            for (int k = 0; k < package_count; k++) {
                scanf("%s", towns[i].post_offices[j].packages[k].id);
                scanf("%d", &towns[i].post_offices[j].packages[k].weight);
            }
        }
    }

    int query_count;
    scanf("%d", &query_count);

    for (int i = 0; i < query_count; i++) {
        int query_type;
        scanf("%d", &query_type);

        if (query_type == 1) {
            char town_name[101];
            scanf("%s", town_name);
            Town *town = find_town_by_name(towns, town_count, town_name);
            print_all_packages(town);
        } else if (query_type == 2) {
            char town_name1[101], town_name2[101];
            int post_office_index1, post_office_index2;
            scanf("%s %d %s %d", town_name1, &post_office_index1, town_name2, &post_office_index2);
            Town *town1 = find_town_by_name(towns, town_count, town_name1);
            Town *town2 = find_town_by_name(towns, town_count, town_name2);
            transfer_packages(town1, post_office_index1, town2, post_office_index2);
        } else if (query_type == 3) {
            Town *most_packages_town = find_town_with_most_packages(towns, town_count);
            printf("Town with the most number of packages is %s\n", most_packages_town->name);
        }
    }

    for (int i = 0; i < town_count; i++) {
        for (int j = 0; j < towns[i].post_office_count; j++) {
            free(towns[i].post_offices[j].packages);
        }
        free(towns[i].post_offices);
    }
    free(towns);

    return 0;
}
